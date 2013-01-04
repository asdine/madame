Tutorial
========

This part of the documentation will help you learn how to use Madame by example.

In this tutorial, we will create a simple address book called MadameBook.

0 - The goal
------------
When you setup a new Madame server, you need to think about what methods you want to be allowed for users and what methods you don't.

For our address book, we want to :

* Get the collection list
* Get the contact list
* Add a new contact
* Get the contact information

But we don't want to be able to:

* Delete the whole contact list
* Delete a contact
* Modify a contact
* Add new collections
* Delete collections

1 - The folders
---------------
Create a folder called **MadameBook** on your computer.

`Download <http://www.mongodb.org/>`_ and install MongoDB anywhere.

2 - The configuration
---------------------
Create a file called **config.py** at the root of your folder, this file will be automatically loaded by Madame.

If you have installed MongoDB on localhost and haven't changed the port, you can skip these lines.

Otherwise, add theses lines in your config file::

  MONGO_HOST = <IP>
  MONGO_PORT = <PORT>

Change <IP> and <PORT> by the actual ip address and port of the server where MongoDB is installed.

3 - The Database Schema
-----------------------
Now, we need to describe our data.

Madame uses JSON format to do so, and `validictory <https://validictory.readthedocs.org/en/latest/>`_ to validate the data.

Create a file called **schemas.json** at the root of your folder.::

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

The first line describes the name of your domain.

It will be used in the url::

  GET http://localhost:5000/contacts/

The value of **"schemas"** follows `validictory <https://validictory.readthedocs.org/en/latest/>`_ format. You can add as much schemas as you want inside this file.

Now, we need to tell Madame about our schema file.

Add this line in your configuration file: ::

  SCHEMA_FILE = "schemas.json"


4 - The methods allowed
-----------------------
Madame is read-only by default. It means that only the GET methods are allowed for the various urls.

Here's what we want to be allowed: ::

  GET       /
  GET       /contacts/
  POST      /contacts/
  GET       /contacts/id/

Here's what is allowed by default: ::

  GET       /
  GET       /contacts/
  GET       /contacts/id/

To add the POST method on our collection, we need to tell it to Madame.
Add the following line in your configuration file: ::

  COLLECTION_POST = True

5 - The server
--------------
Now that our configuration is set, we need to launch the server.

Create a file called **server.py**. ::

  from madame import Madame

  app = Madame()

  app.run()

Now, launch it: ::

  $ python server.py

6 - The final
-------------
To use your beautiful server, you can use `Requests <https://requests.readthedocs.org/en/latest/>`_, curl or Ajax, or anything you want.

Here is an example with curl : ::

  $ curl -i http://localhost:5000/
  HTTP/1.0 200 OK
  Content-Type: application/json
  Content-Length: 313
  Server: Werkzeug/0.8.3 Python/2.7.3
  Date: Fri, 04 Jan 2013 19:59:26 GMT

  {
    "title": "Content",
    "description": "List of collections",
    "links": [
        {
            "href": "http://localhost:5000/",
            "description": "You are here.",
            "rel": "self",
            "title": "root"
        },
        {
            "href": "http://localhost:5000/contacts/",
            "description": "My contact list",
            "rel": "child",
            "title": "Contacts"
        }
    ]
  }

Let's add a new contact : ::

  $ curl -i -d '{ "lastname" : "baggins", "firstname" : "bilbo", "phone-number" : "555-666" }' -H "Content-Type: application/json" http://localhost:5000/contacts/
  HTTP/1.0 201 CREATED
  Content-Type: application/json
  Content-Length: 275
  ETag: "4a98c403225da6cab1b8f5557492a3c370666fe0"
  Server: Werkzeug/0.8.3 Python/2.7.3
  Date: Fri, 04 Jan 2013 20:11:50 GMT

  {
    "title": "Document created",
    "links": [
        {
            "href": "http://localhost:5000/contacts/",
            "description": "You are here.",
            "rel": "self", "title": "Contacts"
        },
        {
            "href": "http://localhost:5000/contacts/50e737860ef3c42120601fae",
            "rel": "item"
        }
    ]
  }

Then let's see the contact information : ::

  $ curl -i http://localhost:5000/contacts/50e737860ef3c42120601fae
  HTTP/1.0 200 OK
  Content-Type: application/json
  Content-Length: 237
  ETag: "494abe2a6a10a3f8d12b93c22e0aa04fb1d5f168"
  Server: Werkzeug/0.8.3 Python/2.7.3
  Date: Fri, 04 Jan 2013 20:14:58 GMT

  {
    "_id": "50e737860ef3c42120601fae",
    "firstname": "bilbo",
    "lastname": "baggins",
    "phone-number": "555-666",
    "created": "Fri Jan  4 20:11:50 2013",
    "updated": "Fri Jan  4 20:11:50 2013",
    "etag": "494abe2a6a10a3f8d12b93c22e0aa04fb1d5f168"
  }

