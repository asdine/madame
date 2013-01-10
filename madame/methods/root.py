from madame.utils import build_url
from werkzeug.exceptions import abort

def get(**pack):
    config = pack['config']
    domains = pack['domains']

    resource = {
        'title' : config['ROOT_TITLE'],
        'description' : config['ROOT_DESCRIPTION']
    }

    children = []
    for collection in domains:
        child = {'url' : build_url(collection)}
        if 'title' in domains[collection]:
            child['title'] = domains[collection]['title']
        if 'description' in domains[collection]:
            child['description'] = domains[collection]['description']
        children.append(child)

    return {'resource' : resource, 'children' : children}, 200

def post(**pack):
    args = pack['args']
    domains = pack['domains']
    app = pack['app']

    domain, content = args.popitem()
    if domain in domains:
        return {'resource' : {'error' : 'ALREADY_EXISTS'}}, 401
    else:
        app.domains[domain] = content

    #: TODO Location-header
    return None, 201


def put(args):
    return None, 405

def patch(args):
    return None, 405

def delete(**pack):
    args = pack['args']
    domains = pack['domains']
    app = pack['app']

    domain, content = args.popitem()
    if domain in domains:
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
