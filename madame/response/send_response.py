from flask import make_response, request, abort
from madame.response.send_json import send_json

mime_table = {
    'default' : send_json,
    'application/json' : send_json
}

def mime_render(data):
    if 'Accept' in request.headers:
        accept = request.headers['Accept']
        if accept in mime_table:
            return mime_table[accept](data), accept
        abort(406)
    return mime_table['default'](data)

def send_response(data=None, status=200, headers=None):
    if not headers: headers = dict()

    msg, mimetype= mime_render(data)
    headers['Content-Type'] = mimetype
    response = make_response((msg, status, headers))
    return response

