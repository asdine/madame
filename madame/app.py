# -*- coding: utf-8 -*-

"""
    Madame.app
    ~~~~~~~~~~

    Module implementing the main Flask application.

    :copyright: (c) 2012 by Asdine El Hrychy.
    :license: MIT, see LICENSE for more details.
"""

import os, logging
from flask import Flask, json, Blueprint, g
from flask.ext.pymongo import PyMongo
from pymongo.errors import ConnectionFailure
from werkzeug.routing import BaseConverter
from .dispatcher import Dispatcher
from .utils import get_main_path
from .methods import default_endpoint_funcs


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

class Madame(Flask):
    """
    Constructs a :class:`Madame <Madame>`.

    Creates a Flask app, load configuration and set a blueprint
    to attach the app at the given url.

    Extends `Flask`
    """

    #: This dictionary will contain the schemas for each collection.
    DOMAINS = {}

    #: This dictionary will contain the endpoints for every request
    endpoint_funcs = {}

    #: Each Madame app can be a blueprint
    #: By default, Madame is set on /, but if a root_url is provided
    #: a blueprint is set instead.
    node = None

    def __init__(self, url_prefix=None, template_folder=None):
        #: If a template folder is provided, Madame will use it
        #: Otherwise, the default Flask template path will be used
        if not template_folder: template_folder = os.path.join(get_main_path(), "templates")

        super(Madame, self).__init__(__package__, template_folder=template_folder)

        #: Save the url_prefix
        self.url_prefix = url_prefix

        #: Set the RegexConverter for custom collection names
        self.url_map.converters['regex'] = RegexConverter

        #: Configuration can be set with both config file and envvar.
        #: Load config from default_settings.py
        self.config.from_object('madame.default_settings')

        #: Try to load it from the file config.py
        try:
            file = os.path.join(get_main_path(), "config.py")
            self.config.from_pyfile(file, silent=False)
        except IOError: pass
        #: Try to load config from the envvar 'MADAME_SETTINGS'
        try:
            self.config.from_envvar('MADAME_SETTINGS', silent=False)
        except RuntimeError: pass

        #: Schemas
        #: A schema file has to be present in the root of the application

        #: Selects a schema file in the configuration
        #: The schema file has to be written in json format
        #: Example, in the config file:
        #:     SCHEMA_FILE = 'schemas.json'
        if 'SCHEMA_FILE' in self.config:
            try:
                with open(self.config['SCHEMA_FILE']) as f:
                    self.DOMAINS = json.loads(f.read())
            except IOError as e:
                logging.error(str(e))
                exit(1)

        #: Load the database handler
        #: TODO support MySQL, PostgresSQL, Redis
        try:
            self.db = PyMongo(self)
            #g.mongo = self.mongo
        except ConnectionFailure as e:
            logging.error(str(e))
            exit(1)

        #: If the user has set an url_prefix for the application,
        #: set and register a blueprint for it.
        if self.url_prefix:
            self.node = Blueprint('madame', __package__, url_prefix=self.url_prefix)
        else: self.node = self

        start_url = '/'
        if 'URL_COLLECTION_RULE' in self.config:
            collection_url = '<regex("%s"):collection>/' % self.config['URL_COLLECTION_RULE']
        else: collection_url = '<collection>'
        #: TODO add configuration value to set the item_url
        item_url = '<ObjectId:id>'

        #: Register endpoints
        dispatcher = Dispatcher.as_view('dispatcher', app=self)
        self.register_endpoint(dispatcher, start_url)
        self.register_endpoint(dispatcher, start_url + collection_url)
        self.register_endpoint(dispatcher, start_url + collection_url + item_url)

        if self.url_prefix:
            self.register_blueprint(self.node)

        #: Set the default endpoint functions
        self.endpoint_funcs = default_endpoint_funcs()

    def register_endpoint(self, obj, url):
        """Registers a route to the Madame blueprint"""
        self.node.add_url_rule(url, view_func=obj, methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])


