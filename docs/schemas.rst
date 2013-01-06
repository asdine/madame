Schemas
=======

Madame doesn't use any python ORM to describe data, it uses JSON schemas to describe each collections. The idea was to separate schemas from code to enable modifications during runtime.
Schemas are considered as part of data, except the fact that they are not saved in the database.

Madame uses `Validictory <http://validictory.readthedocs.org/en/latest/index.html>`_ to validate data with the schemas provided.


There are two ways to add schemas:

- Decribe them in a file
- Add them with a `POST` method on the root url or your API during runtime.

The schema file
---------------
Creating a schema file allows you to set schemas available when your start the application.

These schemas can be disabled with a ``DELETE`` method during runtime if you set the configuration value ``ROOT_DELETE`` to ``True`` in the configuration file.
See :ref:`configuration` section for more details.

To tell Madame about your schema file, add this line in your configuration file : ::

  SCHEMA_FILE = <PATH>

Replace ``<PATH>`` with the path of your schema file.

The schema wrapper
~~~~~~~~~~~~~~~~~~
Schemas are encapsulated in a wrapper that contains additional informations about your collections.

Here is the minimal content that needs to be in your schema file : ::

  {
    <COLLECTION_URL> : {
        "title" : <COLLECTION_TITLE>,
        "description" : <COLLECTION_DESCRIPTION>,
        "schema" : {} # the validictory schema
    },

    <COLLECTION_URL> : ...
  }

=========================== ===============================================================
<COLLECTION_URL>            sets the url of your collection

                            `example` : for "members" -> ``http://localhost:5000/members/``
<COLLECTION_TITLE>          used in the response to describe the given collection
<COLLECTION_DESCRIPTION>    used in the response to describe the given collection
=========================== ===============================================================

To get more informations about how to write schema, see the `Validictory documentation <http://validictory.readthedocs.org/en/latest/index.html>`_, it is very simple and doesn't need to be documented here.

Adding schemas with POST
------------------------
If the configuration value ``ROOT_POST`` is enabled, you can add schemas with a ``POST`` method.
Here is an example with `Requests <https://requests.readthedocs.org/en/latest/>`_ : ::

  >>> import request, json

  >>> schema = { ... }
  >>> headers = {'content-type': 'application/json'}
  >>> r = requests.post('http://localhost:5000/',
  ... data=json.dumps(schema), headers=headers)
  >>> print r.status_code
  201

Schema example
--------------

In the schema file : ::

  {
    # Pet collection
    # url : /pets/
    "pets" : {
        "title" : "Pets",
        "description" : "My pets",
        "schema" : {
            "type" : "object",
            "properties" : {
                "name" : {
                    "type"  : "string",
                    "minLength" : 1,
                    "maxLength" : 15,
                    "required"  : true
                },
                "age" : {
                    "type"  : "number"
                }
            }
        }
    },

    # Book collection
    # url : /books/
    "books" : {
        "title" : "Books"
        "description" : "My book list",
        "schema" : {
            "type" : "object",
            "properties" : {
                "title"     : {"type" : "string", "required" : true},
                "author"    : {"type" : "string", "required" : true}
            }
        }
    }
  }

With the ``POST`` method : ::

  >>> import request, json

  >>> schema = {
  ... "type" : "object",
  ... "properties" : {
  ...     "title"     : {"type" : "string", "required" : true},
  ...     "author"    : {"type" : "string", "required" : true}
  ... }}
  >>> headers = {'content-type': 'application/json'}
  >>> r = requests.post('http://localhost:5000/',
  ... data=json.dumps(schema), headers=headers)
  >>> print r.status_code
  201
