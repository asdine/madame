from flask import request, abort, Response
from flask.views import MethodView, View
from madame.mimetypes import mimeloader
from madame.response import send_response
from madame.response.send_json import jsonify

def get_request_data():
    return request.values.to_dict()

def filter_request_data(app):
    parsed_data = None

    if request.mimetype in app.config['ACCEPTED_MIMETYPE']:
        parsed_data = mimeloader(request.data, request.mimetype)
        if not parsed_data: abort(400)
    else: abort(415)
    return parsed_data

class Dispatcher(View):
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    def __init__(self, app):
        self.app = app

    def dispatch_request(self, collection=None, id=None):
        method = request.method
        resource = 'ROOT'
        pack = {
            'config' : self.app.config,
            'domains': self.app.DOMAINS
        }

        response_type = self.app.config['RESPONSE_TYPE']

        if id: resource = 'ITEM'
        elif collection: resource = 'COLLECTION'

        if id : pack['id'] = id
        if collection: pack['collection'] = collection

        endpoint = "%s_%s" % (resource, method)

        if not self.app.config[endpoint]: abort(405)

        if collection and collection not in self.app.DOMAINS: abort(404)

        if method in ('POST', 'PUT', 'PATCH'):
            pack['args'] = filter_request_data(self.app)
        else:
            pack['args'] = get_request_data()

        response_data = self.app.endpoint_funcs[resource][method](**pack)

        if isinstance(response_data, tuple):

            return send_response(response_type, *response_data)
        elif isinstance(response_data, Response):
            return response_data
        else:
            return send_response(response_type, response_data)
