=============
Predavanja 03
=============


Uvod u upravljanje zavisnostima u programskom jeziku Python
===========================================================

- pip

    - ``sudo pip install ...``, za sve korisnike - *veoma* opasno!
    - ``pip install --user ...``, samo za mog unix korisnika
    - kako imati više verzija jednog istog Python dependency na računaru?

- virtualenv + virtuenanvwrapper::

    mkdir virtualenv_projekat
    cd virtualenv_projekat/
    mkvirtualenv --clear -a . $(basename "`pwd`")

    deactivate

    workon virtualenv_projekat
    pip install Django
    django-admin --version # instaliran Django u virtualenv

    deactivate
    django-admin --version # Django nije sistemstki instaliran, pa je nedostupan van virtualenv

- requirements.txt::

    pip install -r requirements.txt

- poetry - best thing since sliced bread! Njega cemo koristiti na predmetu


Uvod u Django
=============

- create the PDAJ Django project::

    poetry run django-admin startproject pdaj .

- setup the database, run Django migrations and create Django superuser::

    poetry run python manage.py migrate
    poetry run python manage.py createsuperuser

- run the Django project::

    poetry run python manage.py runserver
    xdg-open http://127.0.0.1:8000/
    xdg-open http://127.0.0.1:8000/admin/

- start the ``compute`` Django app, and do the necessary Django setup::

    poetry run python manage.py startapp compute

- create the first (``healtcheck``) Django view, in the ``compute`` Django app

    - view i urlconf


Uvod u razvoj REST API-a kroz Django REST framework
===================================================

- serializers, ``compute.serializers.ComputeParams``
