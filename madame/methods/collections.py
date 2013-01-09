
def get(collection, args):
    return 'COLLECTION GET'

def post(collection, args):
    return 'COLLECTION POST'

def put(collection, args):
    return 'COLLECTION PUT'

def patch(collection, args):
    return 'COLLECTION PATCH'

def delete(collection, args):
    return 'COLLECTION DELETE'

def collection_index():
    index = {
        'GET'   : get,
        'POST'  : post,
        'PUT'   : put,
        'PATCH' : patch,
        'DELETE': delete
    }
    return index
