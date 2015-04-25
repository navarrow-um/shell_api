#!/usr/bin/python
"""Sample shell calls"""

from flask import Flask, jsonify, request
import subprocess
from functools import wraps


def syscall(args):
    """Implement a syscall"""
    salp = ''
    try:
        proc = subprocess.Popen(args,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                universal_newlines=False)
        while proc.poll() is None:
            for line in iter(proc.stdout.readline, ""):
                salp = salp + line
            proc.stdout.flush()
        return salp.strip()
    except OSError as exc:
        return "xecution failed: {}".format(exc)



#APP
app = Flask(__name__)

#Autenticacion
def check_auth(username, password):
    """Validates user and password"""

    if username == "admin" and password == "admin":
        return 1
    else:
        return 0

def authenticate():
    """Shows authentication message"""

    message = {'message': "Authenticate."}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="shell-api"'

    return resp

def requires_auth(f):
    """Makes authentication"""
    @wraps(f)
    def decorated(*args, **kwargs):
        """Makes authentication"""

        auth = request.authorization
        if not auth:
            return authenticate()

        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated

#Error_Handlers
@app.errorhandler(500)
def all_bad(error=None):
    """HTTP 500 Error message"""

    message = {
            'status': 500,
            'message': 'Oops something goes wrong ... -oOo- ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp


@app.errorhandler(404)
def not_found(error=None):
    """HTTP 404 Error message"""

    message = {
            'status': 404,
            'message': 'Sorry this is not here ... ' + request.url,
    }
    resp = jsonify(message)

    resp.status_code = 404
    return resp


@app.errorhandler(400)
def bad_request(error=None):
    """HTTP 400 Error message"""

    message = {
            'status': 400,
            'message': 'Something is wrong on your request ... ' + request.url,
    }
    resp = jsonify(message)

    resp.status_code = 400
    return resp


@app.route('/v1.0/shell', methods=['POST'])
@requires_auth
def shell_exec():
    """Make a syscall with a command and returns JSON output"""

    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            param = request.json
            call = list()
            call = param['args'].split()
            call.insert(0, param['command'])
            output = syscall(call)
            return jsonify(output=output)


@app.route('/v1.0/shell/<command>', methods=['GET'])
def shell_check(command):
    """Make a syscall and check if the command exists"""

    if request.method == 'GET':
        call = list()
        call.insert(0, "which")
        call.append(command)
        output = syscall(call)
        if output == "":
            return jsonify(output="Command not found")
        else:
            return jsonify(output=output)



if __name__ == '__main__':
    app.debug = False
    app.run()
