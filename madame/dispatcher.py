from flask.views import MethodView

class Dispatcher(MethodView):
    def __init__(self, app):
        self.app = app

    def get(self, collection=None, id=None):
        if id:
            return 'Id'
        elif collection:
            return 'Collection'
        else:
            return 'Root'

