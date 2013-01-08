
def get(ressource, args):
    return 'ITEM GET'

def post(ressource, args):
    return 'ITEM POST'

def put(ressource, args):
    return 'ITEM PUT'

def patch(ressource, args):
    return 'ITEM PATCH'

def delete(ressource, args):
    return 'ITEM DELETE'

def item_index():
    index = {
        'GET'   : get,
        'POST'  : post,
        'PUT'   : put,
        'PATCH' : patch,
        'DELETE': delete
    }
    return index
