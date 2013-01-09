
def get(**pack):
    config = pack['config']
    domains = pack['domains']

    resource = {
        'title' : config['ROOT_TITLE'],
        'description' : config['ROOT_DESCRIPTION']
    }

    children = []
    for collection in domains:
        child = {'url' : collection}
        if 'title' in domains[collection]:
            child['title'] = domains[collection]['title']
        if 'description' in domains[collection]:
            child['description'] = domains[collection]['description']
        children.append(child)

    return {'resource' : resource, 'children' : children}, 200

def post(args):
    return 'ROOT POST'

def put(args):
    return 'ROOT PUT'

def patch(args):
    return 'ROOT PATCH'

def delete(args):
    return 'ROOT DELETE'

def root_index():
    index = {
        'GET'   : get,
        'POST'  : post,
        'PUT'   : put,
        'PATCH' : patch,
        'DELETE': delete
    }
    return index
