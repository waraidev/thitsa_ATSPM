import os
import uuid

from flask import Flask, json, jsonify, request, flash, make_response
from flask_cors import CORS
from werkzeug.utils import secure_filename

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
CORS(app)


@app.route('/files', methods=['POST'])
def uploadFiles():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return make_response(jsonify({'result': 'error'}))
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return make_response(jsonify({'result': 'no file selected'}))
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            flash('File successfully uploaded')
            return make_response(jsonify({'result': 'success'}))
        else:
            flash('CSV format is the only allowed file type.')
            return make_response(jsonify({'result': 'wrong file type'}))


@app.route('/files', methods=['GET'])
def getFiles():
    if request.method == 'GET':
        if len(os.listdir(UPLOAD_FOLDER)) == 0:
            flash('No files')
            return make_response(jsonify({'result': 'no file'}))
        else:
            print(os.listdir(UPLOAD_FOLDER))
            return jsonify(os.listdir(UPLOAD_FOLDER))


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
