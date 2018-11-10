# SalesLoft-Eval

Application for SalesLoft interview

This Application was developed in Python using the Django REST framework and integrates with the public SalesLoft API

Django reference -> https://www.django-rest-framework.org/

# Notes for use:

-> Runs with Python version 2.7.15

-> change .env.example to .env and add a valid SalesLoft API key

-> uncomment the lines settings.py that set SALESLOFT_API_KEY and BASE_API_URL via .env

-> make sure to install django as well as the modules listed below

# Must install:

$ pip install django
$ pip install django-environ
$ pip install requests

# Setup notes:

-> make a project directory, then copy the files into it

$ django-admin startproject mysite

-> Apply all mirgrations 

$ python manage.py migrate

-> To run 

$ python manage.py runserver

# Other notes: 

The people directory contains the files/code for the Level 1 app.

The chars directory contains the files/code for the Level 2 app.
