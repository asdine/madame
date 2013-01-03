# -*- coding: utf-8 -*-

"""
    Madame.handler.root
    ~~~~~~~~~~

    Handler for the root url

    :copyright: (c) 2012 by Asdine El Hrychy.
    :license: MIT, see LICENSE for more details.
"""
import json
from flask import request, abort
from flask.views import MethodView
from madame.response import send_response, send_error
from madame.utils import get_collection_link, get_self_link
from simplejson import JSONDecodeError


class RootHandler(MethodView):
    def __init__(self, app, mongo, response_type='json'):
        self.app = app
        self.mongo = mongo

    def get(self):
        """
        Route : GET /
        Returns the list of collections
        """

        if not self.app.config['ROOT_GET']:
            abort(405)

        response = {
            'title' : self.app.config['ROOT_TITLE'],
            'description' : self.app.config['ROOT_DESCRIPTION'],
            'links' : []
        }
        base_url = request.base_url
        response['links'].append(get_self_link(
            title="root",
            base_url=base_url,
            description='You are here.',
            methods=["GET", "POST"]
        ))
        for collection in self.app.DOMAINS:
            response['links'].append(get_collection_link(self.app.DOMAINS, collection, base_url=base_url))
        return send_response(response)

    def post(self):
        """
        Route : POST /
        Description : Creates a collection in the database.
        Returns status
        """

        if not self.app.config['ROOT_POST']:
            abort(405)

        if request.mimetype != 'application/json':
            return send_error(415, "JSON_NEEDED", "Accepted media type : application/json")
        data = request.data
        if isinstance(data, str) or isinstance(data, unicode):
            try:
                data = json.loads(data)
            except JSONDecodeError:
                return send_error(400, "BAD_JSON_FORMAT")
        domain, content = data.popitem()
        if domain in self.app.DOMAINS:
            return send_error(400, message="ALREADY_EXISTS")
        else:
            self.app.DOMAINS[domain] = content
        return send_response(status=201)
