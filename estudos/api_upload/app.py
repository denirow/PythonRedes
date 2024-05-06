from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from functools import wraps
import os

app = Flask(__name__)
api = Api(app)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['USERNAME'] = 'user'
app.config['PASSWORD'] = 'pass'

def check_auth(username, password):
    return username == app.config['USERNAME'] and password == app.config['PASSWORD']

def authenticate():
    message = {'message': "Authentication required."}
    resp = jsonify(message)
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Authentication required."'
    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

class UploadFile(Resource):
    @requires_auth
    def post(self):
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return jsonify({'message': 'File uploaded successfully', 'filename': filename})

api.add_resource(UploadFile, '/upload')

if __name__ == '__main__':
    app.run(ssl_context='adhoc', debug=True)
