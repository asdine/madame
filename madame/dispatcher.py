from flask.views import MethodView

class Dispatcher(MethodView):
    def __init__(self, app):
        self.app = app

    def get(self, collection=None, id=None):
        print 'Collection : %s' % collection
        print 'Id : %s' % id
        return 'Salut'

