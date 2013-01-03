# -*- coding: utf-8 -*-

"""
    Madame.default_settings
    ~~~~~~~~~~~~~~~~~~~~~~~

    Default settings for Flask and Madame

    :copyright: (c) 2012 by Asdine El Hrychy.
    :license: MIT, see LICENSE for more details.
"""

#: DO NOT modify this file!
#: You can write your own configuration file.
#: Two solutions :
#: * Create a file named config.py in the root of your application
#: OR
#: * Set an environnement variable describing the location of your configuration file
#:   and set it wherever you want in your server.

#: ~~~~~ Flask settings ~~~~~~~~

#: Debug is set to True for development and testing purpose
#: Turn it to False in your config file when your application is ready to be deployed.
DEBUG = True

#: ~~~~~ Madame settings ~~~~~~~~

#: For now, the only response type available is json
#: TODO : RESPONSE_TYPE = 'xml'
RESPONSE_TYPE = 'json'

#: Methods
ROOT_GET = True
ROOT_POST = True
ROOT_DELETE = False
COLLECTION_GET = True
COLLECTION_POST = True
COLLECTION_DELETE = False
ITEM_GET = True
ITEM_PUT = False
ITEM_DELETE = False


ROOT_TITLE = 'Content'
ROOT_DESCRIPTION = 'List of collections'
