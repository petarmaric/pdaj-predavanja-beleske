About
=====

Demo za PDAJ predmet, predavanja 4

Quick start
===========

Install the project::

    poetry install

Setup the database, run Django migrations and create Django superuser::

    poetry run python manage.py migrate
    poetry run python manage.py createsuperuser

Run the app::

    poetry run python manage.py runserver
    xdg-open http://127.0.0.1:8000/
    xdg-open http://127.0.0.1:8000/admin/




