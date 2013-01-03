Madame
======

Madame is a dynamic RESTful API for MongoDB based on Flask.


:Author: Asdine El Hrychy
:Version: 0.1

Features
--------
- **REST-compliant**
- **HATEOAS**
- **JSON Schemas separated from code**
- **JSON Validation**
- **Cache**
- **Versioning**


Dynamic
-------
You can add and delete new schemas without turning the servers off and use them immediatly!

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


