from .root import root_index
from .collections import collection_index
from .items import item_index

def default_endpoint_funcs():
    endpoints = {
        'ROOT' : root_index(),
        'COLLECTIONS' : collection_index(),
        'ITEM' : collection_index()
    }
    return endpoints
