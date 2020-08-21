## A REST API Service with Django(2.1.15) and MongoDB(>3.4)
- Create, Retrieve, Update, and Delete tutorials.
- Tutorials have a title, description and published field.
- Tutorials can be serahced for with the title parameter.
- Tutorials that have been published can be listed seperately.

## Setup
- Ensure MongoDB settings are correct in settings.py
- python manage.py makemigrations tutorials
- python manage.py migrate
- python manage.py runserver
