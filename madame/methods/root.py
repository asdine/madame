from madame.utils import build_url
from flask import current_app as app
from werkzeug.exceptions import abort

def get(args):
    resource = {
        'title' : app.config['ROOT_TITLE'],
        'description' : app.config['ROOT_DESCRIPTION']
    }

    children = []
    for collection in app.domains:
        child = {'url' : build_url(collection)}
        if 'title' in app.domains[collection]:
            child['title'] = app.domains[collection]['title']
        if 'description' in app.domains[collection]:
            child['description'] = app.domains[collection]['description']
        children.append(child)

    return {'resource' : resource, 'children' : children}, 200

def post(args):
    domain, content = args.popitem()
    if domain in app.domains:
        return {'resource' : {'error' : 'ALREADY_EXISTS'}}, 401
    else:
        app.domains[domain] = content

    #: TODO Location-header
    return None, 201


def put(args):
    return None, 405

def patch(args):
    return None, 405

def delete(args):
    domain, content = args.popitem()
    if domain in app.domains:
        del app.domains[domain]
    else:
        abort(404)
    return None, 204

def root_index():
    index = {
        'GET'   : get,
        'POST'  : post,
        'PUT'   : put,
        'PATCH' : patch,
        'DELETE': delete
    }
    return index
