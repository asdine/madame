# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='madame',
    version='0.1.0',
    packages=find_packages(),
    url='http://github.com/asdine/madame',
    author='Asdine El Hrychy',
    author_email='asdine.elhrychy@gmail.com',
    description='RESTful API for MongoDB built on Flask',
    long_description=open('README.rst').read(),
    include_package_data=True,
    install_requires=['flask', 'flask-pymongo', 'simplejson', 'validictory'],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Intended Audience :: Developers",
        "Environment :: Web Environment"
        ]
)
