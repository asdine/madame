
def get(collection, id, args):
    return 'ITEM GET'

def post(collection, id, args):
    return 'ITEM POST'

def put(collection, id, args):
    return 'ITEM PUT'

def patch(collection, id, args):
    return 'ITEM PATCH'

def delete(collection, id, args):
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
