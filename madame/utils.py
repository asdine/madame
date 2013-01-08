# -*- coding: utf-8 -*-

"""
    Madame.utils
    ~~~~~~~~~~

    Useful functions.

    :copyright: (c) 2012 by Asdine El Hrychy.
    :license: MIT, see LICENSE for more details.
"""

import json
import sys
import urlparse
from bson import ObjectId
import os, hashlib
from werkzeug.routing import BaseConverter


def get_etag(value):
    """Generates an etag for the given document.
    :param value: Document
    """
    h = hashlib.sha1()
    h.update(str(value))
    return h.hexdigest()

def get_collection_link(domains, collection, base_url='/'):
    domain = domains[collection]
    link = {}
    if 'title' in domain:
        link['title'] = domain['title']
    if 'description' in domain:
        link['description'] = domain['description']
    if 'methods' in domain:
        link['methods'] = domain['methods']
    link['href'] = os.path.join(base_url, collection + '/')
    link['rel'] = 'child'
    return link

def get_document_link(document, base_url='/'):
    link = {'href': os.path.join(base_url, str(document['_id'])), 'rel': 'item'}
    return link

def get_parent_link(base_url='/'):
    link = {'rel' : 'parent'}
    parts = urlparse.urlparse(base_url)
    path = parts.path
    if path.endswith('/'): path = path[:-1]
    frags = path.split('/')
    path = '/'.join(frags[:-1]) + '/'
    Parse = urlparse.ParseResult(parts.scheme, parts.netloc, path, '', '', '')
    link['href'] = urlparse.urlunparse(Parse)
    return link

def get_self_link(title='', base_url='/', description='', methods=None):
    if not methods: methods = []
    link = {
        'title' : title,
        'href'  : base_url,
        'rel'   : 'self',
        'description' : description,
        'methods' : methods
    }
    return link

def get_package_home(context):
    """Shorcut"""
    return os.path.dirname(context["__file__"])

def get_execution_path(context, filename):
    """Shorcut"""
    return os.path.join(get_package_home(context), filename)

def get_main_path():
    """Shorcut"""
    return os.path.abspath(os.path.dirname(sys.argv[0]))

def format_args(obj):
    """
    Filter request args
    :param obj: request args
    :return: filtered args and directives
    """
    opts = {}
    args = {}
    for arg in obj:
        if arg == "where":
            args = json.loads(obj['where'])
        elif arg == "_id":
            args["_id"] = ObjectId(obj['_id'])
        elif arg == "limit":
            opts["limit"] = int(obj["limit"])
        elif arg == "skip":
            opts["skip"] = int(obj["skip"])
        else:
            args[arg] = obj[arg]
    return args, opts
