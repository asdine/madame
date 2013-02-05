from flask import request, abort, Response
from flask import current_app as app
from flask.views import View
from madame.mimetypes import mimeloader
from madame.response import send_response
from madame.utils import unpack_response_data

def get_request_data():
    return request.values.to_dict()

def filter_request_data(app):
    parsed_data = None

    if request.mimetype in app.config['ACCEPTED_MIMETYPES']:
        parsed_data = mimeloader(request.data, request.mimetype)
        if not parsed_data: abort(400)
    else: abort(415)
    return parsed_data

class Dispatcher(View):
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    def dispatch_request(self, collection=None, id=None):
        method = request.method
        resource = 'ROOT'
        renderer = app.config['RENDERER']
        pack = {
            'app' : app,
            'config' : app.config,
            'domains': app.domains
        }
        print request.accept_mimetypes
        headers = None
        status = 200
        response = ''

        if id: resource = 'ITEM'
        elif collection: resource = 'COLLECTION'

        if id : pack['id'] = id
        if collection: pack['collection'] = collection

        endpoint = "%s_%s" % (resource, method)

        if not app.config[endpoint]: abort(405)

        if collection and collection not in app.domains: abort(404)

        if method in ('POST', 'PUT', 'PATCH'):
            pack['args'] = filter_request_data(app)
        else:
            pack['args'] = get_request_data()

        response_data = app.endpoint_funcs[resource][method](pack)
        if isinstance(response_data, tuple):
            data, status, headers = unpack_response_data(*response_data)
        elif isinstance(response_data, Response):
            return response_data
        else: data = response_data

        if data:
            rnd = app.renderer_funcs[renderer]()
            response = getattr(rnd, resource.lower())(data)
        return send_response(response, status, headers)

