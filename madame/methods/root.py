
def get(args):
    return 'ROOT GET', 'wesh', 201

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
