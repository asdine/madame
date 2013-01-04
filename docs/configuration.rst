Configuration
=============

Madame doesn't necessarily need a configuration file, but it can be very helpful to create one if you want to change your server's behaviour.

Configuration file
------------------
As Flask, Madame can handle configuration in two ways.

You can choose between of those two, or use both for one to be more global and the other more specific.

From an environment variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Create your file wherever you want on your server. Then, you need to create an environment variable called ``MADAME_SETTINGS`` and set its value with the path of your file. ::

  $ touch /path/to/your/configfile.py
  $ export MADAME_SETTINGS=/path/to/your/configfile.py

From the root of your application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Create the file at the root of your application.
The file name has to be ``config.py``.
::

  $ cd /path/to/your/application
  $ touch config.py

Builtin configuration values
----------------------------
You can use all of the `Flask configuration values <http://flask.pocoo.org/docs/config/#builtin-configuration-values>`_.

Madame has also its own values:

+-------------------+-------------------------------------------------------+-------------------------------------+
| Option            | Description                                           | Default value                       |
+===================+=======================================================+=====================================+
| SCHEMA_FILE       | describes the name of the schema file                 | ``None``                            |
+-------------------+-------------------------------------------------------+-------------------------------------+
| ROOT_GET          | enable/disable GET method on root                     | ``True``                            |
+-------------------+-------------------------------------------------------+-------------------------------------+
| ROOT_POST         | enable/disable POST method on root                    | ``False``                           |
+-------------------+-------------------------------------------------------+-------------------------------------+
| ROOT_DELETE       | enable/disable DELETE method on root                  | ``False``                           |
+-------------------+-------------------------------------------------------+-------------------------------------+
| COLLECTION_GET    | enable/disable GET method on collections              | ``True``                            |
+-------------------+-------------------------------------------------------+-------------------------------------+
| COLLECTION_POST   | enable/disable POST method on collections             | ``False``                           |
+-------------------+-------------------------------------------------------+-------------------------------------+
| COLLECTION_DELETE | enable/disable DELETE method on collections           | ``False``                           |
+-------------------+-------------------------------------------------------+-------------------------------------+
| ITEM_GET          | enable/disable GET method on items                    | ``True``                            |
+-------------------+-------------------------------------------------------+-------------------------------------+
| ITEM_PUT          | enable/disable PUT method on items                    | ``False``                           |
+-------------------+-------------------------------------------------------+-------------------------------------+
| ITEM_DELETE       | enable/disable DELETE method on items                 | ``False``                           |
+-------------------+-------------------------------------------------------+-------------------------------------+
| ROOT_TITLE        | sets the root title that is displayed in responses    | ``'Content'``                       |
+-------------------+-------------------------------------------------------+-------------------------------------+
| ROOT_DESCRIPTION  | sets the root title that is displayed in responses    | ``'List of collections'``           |
+-------------------+-------------------------------------------------------+-------------------------------------+

