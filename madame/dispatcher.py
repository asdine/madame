from flask.views import MethodView

#: TODO root_handler, collection_handler, item_handler

class Dispatcher(MethodView):
    def __init__(self, app):
        self.app = app

    def get(self, collection=None, id=None):
        #:

        #: /collection/id
        if id:
            return 'Id'
        #: /collection/
        elif collection:
            return 'Collection'
        #: /
        else:

            return 'Root'

