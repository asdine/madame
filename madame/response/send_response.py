from flask import make_response
from madame.response.send_json import send_json

mime_table = {
    'json' : send_json
}

def send_type(type, data):
    if type in mime_table:
        return mime_table[type](data)
    return ''

def send_response(response_type='json', data=None, status=200, headers=None):
    msg = send_type(response_type, data)
    response = make_response((msg, status, headers))
    return response

