import os
import uuid

from flask import Flask, jsonify, request, flash, make_response
from flask_cors import CORS
from werkzeug.utils import secure_filename

from helpers import upload_file_s3, get_files_s3, delete_file_s3
from config import s3_bucket

path = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(path, "upload/")

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024
app.secret_key = uuid.uuid4().hex

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
        output = upload_file_s3(file, s3_bucket())
        flash('File successfully uploaded')
        return make_response(jsonify({'result': 'success, {}'.format(output)}))


@app.route('/files', methods=['GET'])
def getFiles():
    if request.method == 'GET':
        filenames = get_files_s3(s3_bucket())
        if len(filenames) == 0:
            flash('No files')
            return make_response(jsonify({'result': 'no files'}))
        else:
            print(filenames)
            return jsonify(filenames)


@app.route('/files/<filename>', methods=['DELETE'])
def deleteFile(filename):
    if request.method == 'DELETE':
        if len(os.listdir(UPLOAD_FOLDER)) == 0:
            flash('No files')
            return make_response(jsonify({'result': 'No file to delete'}))
        file = request.files['file']
        if file and filename == file.filename:
            os.remove(os.path.join(UPLOAD_FOLDER, filename))
            return make_response(jsonify({'result': 'File removed.'}))
        else:
            return make_response(jsonify({'result': 'Something went wrong!'}))


if __name__ == '__main__':
    app.run()
