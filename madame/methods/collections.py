
def get(ressource, args):
    return 'COLLECTION GET'

def post(ressource, args):
    return 'COLLECTION POST'

def put(ressource, args):
    return 'COLLECTION PUT'

def patch(ressource, args):
    return 'COLLECTION PATCH'

def delete(ressource, args):
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
