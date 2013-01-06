.. Madame documentation master file, created by
   sphinx-quickstart on Thu Jan  3 16:08:39 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Madame
=================

Release v0.1.2. (:ref:`installation`)

Welcome to Madame's documentation.
Madame is a RESTful API for MongoDB built on Flask.
It is highly customizable and easy to use and to configure.

::

  from madame import Madame

  app = Madame()
  app.run()


Madame depends on two main libraries: the `Flask <http://flask.pocoo.org/>`_ microframework and the `Validictory <http://validictory.readthedocs.org/en/latest/index.html>`_ data validator.
These libraries are not documented here. If you want to dive into their documentation, check out the following links:

- `Flask documentation <http://flask.pocoo.org/docs/>`_
- `Validictory documentation <http://validictory.readthedocs.org/en/latest/index.html>`_

User’s Guide
------------

.. toctree::
   :maxdepth: 2

   intro
   install
   quickstart
   tutorial
   configuration
   schemas

