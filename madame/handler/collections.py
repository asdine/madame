# -*- coding: utf-8 -*-

"""
    Madame.handler.collections
    ~~~~~~~~~~

    Handler for collections.

    :copyright: (c) 2012 by Asdine El Hrychy.
    :license: MIT, see LICENSE for more details.
"""

from datetime import datetime
from flask.helpers import json
from flask.views import MethodView
from madame.response import send_response, send_error
from madame.utils import get_etag, format_args, get_document_link, get_self_link, get_parent_link
from madame.validator import Validator
from flask import request
from simplejson import JSONDecodeError
from werkzeug.exceptions import abort

class CollectionsHandler(MethodView):
    def __init__(self, app, mongo, response_type='json'):
        self.app = app
        self.mongo = mongo

    def get(self, collection):
        """
        Route : GET /<collection>/
        Description : Gets the list of documents in the given collection
        filtered with the given filters
        Returns a list of documents with etag.
        """

        if not self.app.config['COLLECTION_GET']:
            abort(405)

        if collection not in self.app.DOMAINS:
            abort(404)
        args = request.values.to_dict()
        if args:
            args, opts = format_args(args)
            cursor = self.mongo.db[collection].find(args, **opts)
        else:
            cursor = self.mongo.db[collection].find(limit=20)
        base_url = request.base_url

        #: Building response
        response = {'links' : [], 'title' :'', 'description' : ''}
        if 'title' in self.app.DOMAINS[collection]:
            response['title'] = self.app.DOMAINS[collection]['title']
        if 'description' in self.app.DOMAINS[collection]:
            response['description'] = self.app.DOMAINS[collection]['description']

        response['links'].append(get_self_link(
            title=response['title'],
            base_url=base_url,
            description='You are here.',
            methods=["GET", "POST", "DELETE"]
        ))
        response['links'].append(get_parent_link(base_url))
        for document in cursor:
            response['links'].append(get_document_link(document, base_url))
        return send_response(response)

    def post(self, collection):
        """
        Route : POST /<collection>/
        Description : Creates a list of documents in the database.
        Returns status and _id for each document.
        """

        if not self.app.config['COLLECTION_POST']:
            abort(405)

        if collection not in self.app.DOMAINS:
            abort(404)
        if request.mimetype != 'application/json':
            return send_error(415, "JSON_NEEDED", "Accepted media type : application/json")
        data = request.data
        if not data:
            return send_error(400, "EMPTY_DATA")
        if isinstance(data, str) or isinstance(data, unicode):
            try:
                data = json.loads(data)
            except JSONDecodeError:
                return send_error(400, "BAD_JSON_FORMAT")
        if isinstance(data, dict):
            status = self.validate(data, collection)
            if status['created']:
                base_url = request.base_url
                response = {'title': "Document created", 'links': []}
                response['links'].append(get_self_link(
                    title=self.app.DOMAINS[collection]['title'],
                    base_url=base_url,
                    description='You are here.',
                    methods=["GET", "POST", "DELETE"]
                ))
                response['links'].append(get_document_link(status['document'], base_url))
                return send_response(response, 201, get_etag(status['document']))
            else:
                return send_error(400, "VALIDATION_ERROR", status['issues'])
        return send_error(400, "BAD_DATA_FORMAT")

    def delete(self, collection):
        """
        Route : DELETE /<collection>/
        Description : Deletes every document in the given collection.
        Returns status
        """

        if not self.app.config['COLLECTION_DELETE']:
            abort(405)

        if collection not in self.app.DOMAINS:
            abort(404)
        self.mongo.db[collection].drop()
        return send_response('')

    def validate(self, item, collection):
        date_utc = datetime.utcnow()
        v = Validator()
        if v.validate(item, self.app.DOMAINS[collection]['schema']):
            item['created'] = item['updated'] = date_utc
            item['_id'] = self.mongo.db[collection].insert(item)
            response = ({'created' : True, 'document' : item})
        else:
            response = ({'created' : False, 'issues' : v.error})
        return response