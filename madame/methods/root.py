
def get(ressource, args):
    return 'ROOT GET'

def post(ressource, args):
    return 'ROOT POST'

def put(ressource, args):
    return 'ROOT PUT'

def patch(ressource, args):
    return 'ROOT PATCH'

def delete(ressource, args):
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
