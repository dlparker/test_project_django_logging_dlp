.. role:: python(code)
    :language: python

Django Logging DLP Fork Test Project
====================================

Django project used to test the DLP fork of django-logging-json. https://github.com/dlparker/django-logging

Setup
============

.. code-block:: python

   (virtualenv) pip install -r requirements.txt
   (virtualenv) ./manage.py migrate


Running tests
=============

.. code-block:: python

   (virtualenv) ./manage.py test targets

Change Log
==================

       [2017-1-18] 11:30 CDT

Initial project with a few tests and no integration (or testing) of django-logging-json
