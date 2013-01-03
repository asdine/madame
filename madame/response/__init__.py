from flask import make_response
from madame.response.send_json import send_json

def send_response(obj=None, status=200, etag=None):
    if not obj:
        response = make_response('')
    else:
        response = make_response(send_json(obj))
    if etag:
        response.set_etag(etag)
    response.status_code = status
    return response

def send_error(status, type='', message=''):
    error = {'error' : type}
    if message:
        error["message"] = message
    response = make_response(send_json(error))
    response.status_code = status
    return response
