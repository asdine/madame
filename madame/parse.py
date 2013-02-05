from flask import has_request_context, request

class ParseRequest():
    headers = None
    accept = None
    etag = None
    if_modified_since = None
    if_none_match = None

    page = 1

    sort = None
    filter = None
    limit = 20

    def __init__(self):
        if not has_request_context(): return

        self.headers = request.headers
        
        self.accept = request.accept_mimetypes.best_match(['application/json'])



