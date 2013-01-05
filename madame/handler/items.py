# -*- coding: utf-8 -*-

"""
    Madame.handler.items
    ~~~~~~~~~~

    Handler for documents.

    :copyright: (c) 2012 by Asdine El Hrychy.
    :license: MIT, see LICENSE for more details.
"""

from datetime import datetime
from flask import request
from flask.helpers import json
from flask.views import MethodView
from madame.response import send_response, send_error
from madame.utils import get_etag
from madame.validator import Validator
from simplejson import JSONDecodeError
from werkzeug.exceptions import abort

class ItemsHandler(MethodView):
    def __init__(self, app, mongo):
        self.app = app
        self.mongo = mongo

    def get(self, collection, id):
        """
        Route : GET /<collection>/<id>
        Description : Gets the chosen document.
        Returns the document.
        """

        if not self.app.config['ITEM_GET']:
            abort(405)

        if collection not in self.app.DOMAINS:
            abort(404)
        document = self.mongo.db[collection].find_one_or_404({"_id" : id})
        document['etag'] = get_etag(document)
        return send_response(document, etag=document['etag'])

    def put(self, collection, id):
        """
        Route : PUT /<collection>/<id>
        Description : Updates the document.
        Returns the status.
        """

        if not self.app.config['ITEM_PUT']:
            abort(405)

        if collection not in self.app.DOMAINS:
            abort(404)
        document = self.mongo.db[collection].find_one_or_404({"_id" : id})
        date_utc = datetime.utcnow()
        if request.mimetype != 'application/json':
            return send_error(415, "JSON_NEEDED", "Accepted media type : application/json")
        data = request.data
        if isinstance(data, str) or isinstance(data, unicode):
            try:
                data = json.loads(data)
            except JSONDecodeError:
                return send_error(400, "BAD_JSON_FORMAT")
        for key in data:
            document[key] = data[key]
        copy = {}
        for key in document:
            if key == "created": continue
            if key == "updated": continue
            if key == "_id": continue
            copy[key] = document[key]
        v = Validator()
        if v.validate(copy, self.app.DOMAINS[collection]['schema']):
            document['updated'] = date_utc
            self.mongo.db[collection].save(document)
            return send_response(status=200)
        return send_error(400, "VALIDATION_ERROR", v.error)

    def delete(self, collection, id):
        """
        Route : DELETE /<collection>/<id>
        Description : Deletes the document from the collection.
        Returns the status.
        """

        if not self.app.config['ITEM_DELETE']:
            abort(405)

        if collection not in self.app.DOMAINS:
            abort(404)
        document = self.mongo.db[collection].find_one_or_404({"_id": id})
        self.mongo.db[collection].remove(document)
        return send_response(status=200)
