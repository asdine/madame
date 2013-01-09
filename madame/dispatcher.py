from flask import request, abort
from flask.views import MethodView, View
from madame.response import send_response
from madame.response.send_json import jsonify

def get_request_data():
    return request.values.to_dict()

def filter_request_data(app):
    if request.mimetype in app.config['ACCEPTED_MIMETYPE']:
        return request.data
    return None

class Dispatcher(View):
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    def __init__(self, app):
        self.app = app

    def dispatch_request(self, collection=None, id=None):
        method = request.method
        resource = 'ROOT'
        kwargs = {}
        data = ''
        headers = {}
        status = 200

        if id: resource = 'ITEM'
        elif collection: resource = 'COLLECTION'

        if id : kwargs['id'] = id
        if collection: kwargs['collection'] = collection

        endpoint = "%s_%s" % (resource, method)

        if method in ('POST', 'PUT', 'PATCH'):
            args =
        kwargs['args'] = get_request_data()


        if not self.app.config[endpoint]: abort(405)
        if collection and collection not in self.app.DOMAINS: abort(404)

        response_data = self.app.endpoint_funcs[resource][method](**kwargs)

        if isinstance(response_data, tuple):
            return send_response(*response_data)
        else: return send_response(response_data)

