# -*- coding: utf-8 -*-

"""
    Madame.app
    ~~~~~~~~~~

    Module implementing the main Flask application.

    :copyright: (c) 2012 by Asdine El Hrychy.
    :license: MIT, see LICENSE for more details.
"""

import os, logging
from flask import Flask, json, Blueprint
from flask.ext.pymongo import PyMongo
from madame.handler.root import RootHandler
from madame.handler.collections import CollectionsHandler
from madame.handler.items import ItemsHandler
from madame.utils import get_main_path
from pymongo.errors import ConnectionFailure

class Madame(Flask):
    """
    Constructs a :class:`Madame <Madame>`.

    Creates a Flask app, load configuration and set a blueprint
    to attach the app at the given url.

    Extend `Flask`
    """
    def __init__(self, root_url=None, template_folder=None):
        """

        :param root_url: root url for Madame
        :param template_folder:
            sets a different template folder
        """
        if template_folder is None:
            template_folder = os.path.join(get_main_path(), "templates")
        super(Madame, self).__init__(__package__, template_folder=template_folder)
        self.load_config()
        self.init_database()
        self.load_schemas()
        self.register(root_url)

    def load_config(self):
        """Loads config from default_settings.py, then tries to
         load it from the file config.py and, if it fails,
         loads it from the envvar 'MADAME_SETTINGS'

         Defaults :
         DEBUG is set to TRUE
        """
        self.config.from_object('madame.default_settings')
        try:
            file = os.path.join(get_main_path(), "config.py")
            self.config.from_pyfile(file, silent=False)
        except IOError:
            pass
        try:
            self.config.from_envvar('MADAME_SETTINGS', silent=False)
        except RuntimeError:
            pass

    def init_database(self):
        """ Tries to etablish a connection to the database.
        Uses the MongoDB default IP address (localhost) and port (27017).
        To select another IP address and port number, set it in the config file.
        Example :
        MONGO_HOST = <IPADDRESS>
        MONGO_PORT = <PORT>
        """
        try:
            self.mongo = PyMongo(self)
        except ConnectionFailure as e:
            logging.error(str(e))
            exit(1)

    def load_schemas(self):
        """A schema file has to be present in the root of your application"""

        #: Selects a schema file in your config
        #: The schema file has to be written in json format
        #: Example, in your config file:
        #:     SCHEMA_FILE = 'schemas.json'
        if 'SCHEMA_FILE' not in self.config:
            self.DOMAINS = {}
            return
        try:
            with open(self.config['SCHEMA_FILE']) as f:
                self.DOMAINS = json.loads(f.read())
        except IOError as e:
            logging.error(str(e))
            exit(1)

    def register(self, root_url):
        """If the user has chosen a root url for the application,
        this function sets and register a blueprint for it.
        """
        if root_url is not None:
            self.root = Blueprint('madame', __package__, url_prefix=root_url)
        else:
            self.root = self
        self.init_routes()
        if root_url is not None:
            self.register_blueprint(self.root)

    def init_routes(self):
        """ Creates all the routes

        / GET, POST, PATCH
        /<collectionname> GET, POST, DELETE
        /<collectionname>/<document>/ GET, PATCH, DELETE
        See :class:`Madame.handler.CollectionHandler` for more information.
        """
        root = RootHandler.as_view('root', app=self, mongo=self.mongo)
        collections = CollectionsHandler.as_view('collection', app=self, mongo=self.mongo)
        items = ItemsHandler.as_view('items', app=self, mongo=self.mongo)
        self.root.add_url_rule('/', view_func=root, methods=['GET', 'POST', 'PATCH'])
        self.root.add_url_rule('/<string:collection>/', view_func=collections, methods=['GET', 'POST', 'DELETE'])
        self.root.add_url_rule('/<string:collection>/<ObjectId:id>', view_func=items, methods=['GET', 'PATCH', 'DELETE'])

