Madame
======

Madame is a dynamic RESTful API for MongoDB based on Flask.


:Author: Asdine El Hrychy
:Version: 0.1

Features
--------
- **REST-compliant**
- **HATEOAS**
- **Dynamic collections**
- **JSON Schemas separated from code**
- **JSON Validation**
- **Cache**
- **Versioning**
- **Read-only by default**

CRUD
----
Madame supports built-in CRUD operations.

    ======= ======
    Action  Method
    ======= ======
    Create  POST
    Read    GET
    Update  PATCH
    Update* POST
    Delete  DELETE
    ======= ======

*Update method can use POST or PATCH, whether the user updates the entire document or not.

Schemas
-------
Madame keep database schemas separated from code, and uses JSON to describe them.
To validate the data, it uses the strong schema validation library : `Validictory <https://github.com/sunlightlabs/validictory>`_. ::

  {
      "contacts": {
            "title"     : "Contacts",
            "description" : "My contact list",
            "schema"    : {
                "type" : "object",
                "properties" : {
                    "firstname" : {
                        "type"  : "string",
                        "minLength" : 1,
                        "maxLength" : 10
                    },
                    "lastname"  : {
                        "type"  : "string",
                        "minLength" : 1,
                        "maxLength" : 15,
                        "required"  : true
                    },
                    "phone-number" : {
                        "type"  : "string",
                        "format": "phone"
                    }
                }
            }
      }
  }


Dynamic
-------
You can add and delete new schemas without turning the servers off and use them immediatly. ::

  >>> import requests, json

  >>> data = {
        "pets" :
            {
                "title": "Pets",
                "description" : "My pets",
                "schema" :
                    {
                        "type" : "object",
                        "properties" : {
                            "name" : {
                                "type"  : "string",
                                "minLength" : 1,
                                "maxLength" : 15,
                                "required"  : True
                            }
                        }
                    }
            }
      }
  >>> headers = {'content-type': 'application/json'}
  >>> r = requests.post('http://localhost:5000/', data=json.dumps(data), headers=headers)
  >>> print r.status_code
  201

You can then add new pets on your collection. ::

  $ curl -i -d '{ "name" : "Betise" }' -H "Content-Type: application/json" http://localhost:5000/pets/
  HTTP/1.0 201 CREATED
  Content-Type: application/json
  Content-Length: 263
  ETag: "17c62e0fd3f85bf0f7db76fc2c90027f3309a83c"
  Server: Werkzeug/0.8.3 Python/2.7.3
  Date: Fri, 04 Jan 2013 15:36:00 GMT

  {
    "title": "Document created",
    "links":
        [
            {
                "methods": ["GET", "POST", "DELETE"],
                "href": "http://localhost:5000/pets/",
                "description": "You are here.",
                "rel": "self",
                "title": "Pets"
            },
            {
                "href": "http://localhost:5000/pets/50e6f6e00ef3c414fcf66b45",
                "rel": "item"
            }
        ],
  }


Filtering and sorting
---------------------
Madame uses MongoDB options for filtering and sorting. ::

  $ curl http://localhost:5000/pets/?limit=1&skip=20

Installation
------------
::

    $ pip install madame

Usage
-----
::

    from madame import Madame

    app = Madame()
    app.run()


Versioning
----------
::

    from madame import Madame

    app = Madame('/v1')
    app.run()


Flask and Ajax
--------------
Use Madame as an Ajax extension of your website.
As Madame is built on Flask, you can still use it as a normal website.
::

    from madame import Madame
    from flask import render_template

    app = Madame('/ajax')
    app.run()

    @app.route('/')
    def index():
        return render_template('index.html')

    if __name__ == "__main__":
        app.run()


Future
------
- Highly customizable
- Authentication
- Pagination
- GET /<collection>/<chosenIdentifier>

and so on.

Feedback
--------
Any comment or advice would be highly appreciated!

Documentation
-------------
Complete documentation is available at `https://madame.readthedocs.org <https://madame.readthedocs.org>`_

License
-------
Madame is MIT licensed. See the `LICENSE <https://github.com/asdine/madame/blob/master/LICENSE>`_ for details.

Credits
-------
`Flask <http://flask.pocoo.org/>`_

`Pymongo <http://api.mongodb.org/python/current/>`_

`Validictory <https://github.com/sunlightlabs/validictory>`_

Authors
-------
Madame is developped by Asdine El Hrychy.
See the `AUTHORS <https://github.com/asdine/madame/blob/master/AUTHORS>`_ for details.

