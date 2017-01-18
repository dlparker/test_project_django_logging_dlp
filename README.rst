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

Handler Override tests
======================

The full set of tests includes a test of an added handler. To test the feature
of fully overriding the handlers defined by the library you can use the "replace_settings.py" file. To just test that one feature:

.. code-block:: python

   (virtualenv) ./manage.py test targets.tests.LogsAddHandlerTest --settings=test_server_django_logging.replace_settings



Change Log
==================
[2017-1-18] 15:30 CDT

Added integration and testing of django-loggin-json. Includes use of custom handler in both extra and override mode.


[2017-1-18] 11:30 CDT

Initial project with a few tests and no integration (or testing) of django-logging-json
