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

  SCHEMAS_FILE = "schemas.json"


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


