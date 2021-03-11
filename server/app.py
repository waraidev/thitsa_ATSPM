from flask import Flask, jsonify, request, flash, make_response
from flask_cors import CORS
from werkzeug.utils import secure_filename
from io import BytesIO
import base64

from aws_helpers import upload_file_s3, get_all_files_s3, delete_file_s3
from aws_helpers import get_file_url, get_signal_name, get_image_url
from config import s3_file_bucket, s3_image_bucket
import config
from simpls.SIMPLS import SIMPLS_Chart

# See aws_helpers.py for details on config file not in Git
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = config.app_secret_key()
app.debug = config.debug()

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/files', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return make_response(jsonify({'result': 'error'}))
    file = request.files['file']
    if file.filename == '':
        flash('No file selected for uploading')
        return make_response(jsonify({'result': 'no file selected'}))
    if file:
        file.filename = secure_filename(file.filename)
        output = upload_file_s3(file, s3_file_bucket())
        flash('File successfully uploaded')
        return make_response(jsonify({'result': 'success, {}'.format(output)}))


@app.route('/files', methods=['GET'])
def get_files():
    if request.method == 'GET':
        filenames = get_all_files_s3(s3_file_bucket())
        if len(filenames) == 0:
            flash('No files')
            return make_response(jsonify({'result': 'no files'}))
        else:
            print(filenames)
            return jsonify(filenames)


@app.route('/images', methods=['GET'])
def get_image_names():
    if request.method == 'GET':
        image_names = get_all_files_s3(s3_image_bucket())
        if len(image_names) == 0:
            flash('No images')
            return make_response(jsonify({'result': 'no images'}))
        else:
            return jsonify(image_names)


@app.route('/images/<image_name>', methods=['GET'])
def get_image(image_name):
    if request.method == 'GET':
        if image_name not in get_all_files_s3(s3_image_bucket()):
            flash('Image cannot be found')
            return make_response(jsonify({'result': 'Image cannot be found'}))

        # function from aws_helper.py
        return get_image_url(image_name)


@app.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    if request.method == 'DELETE':
        if filename not in get_all_files_s3(s3_file_bucket()):
            flash('File does not exist')
            return make_response(jsonify({'result': 'File does not exist.'}))
        output = delete_file_s3(filename, s3_file_bucket())

        return make_response(jsonify(
            {'result': 'success, {}'.format(output)}
        ))


@app.route('/plot/<filename>', methods=['GET'])
def get_plot(filename):
    if request.method == 'GET':
        if filename not in get_all_files_s3(s3_file_bucket()):
            flash('File does not exist')
            return make_response(jsonify({'result': 'File does not exist.'}))
        file_url = get_file_url(filename)

        image = SIMPLS_Chart(file_url, filename)

        image_file = BytesIO(base64.b64decode(image[22:]))
        upload_file_s3(image_file, s3_image_bucket(), get_signal_name(filename))

        return image


if __name__ == '__main__':
    app.run()
