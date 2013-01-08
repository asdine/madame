from .root import root_index
from .collections import collection_index
from .items import item_index

def default_endpoint_funcs():
    endpoints = {
        'root' : root_index(),
        'collections' : collection_index(),
        'item' : collection_index()
    }
    return endpoints
