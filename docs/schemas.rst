Schemas
=======

Madame doesn't use any python ORM to describe data, it uses JSON schemas. The idea was to separate schemas from code to enable modifications during runtime.
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


