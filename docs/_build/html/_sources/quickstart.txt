Usage
=====

Using Madame is very simple.

Prerequisites
-------------
Madame needs MongoDB to work properly.
To do so, install it from `MongoDB's website <http://www.mongodb.org/>`_.

Basic usage
-----------
First, import the module::

  >>> from madame import Madame

Then instantiate the Madame class::

  >>> app = Madame()

Finally, run it::

  >>> app.run()


Without configuration, your application is read-only and with no schemas.
You would probably want to enable some collections. Go to the :ref:`tutorial` section to see how easy it is to configure Madame applications.

