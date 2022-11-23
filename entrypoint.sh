#!/bin/sh

set -e

#ln -s /usr/local/lib/python3.7/site-packages/django/contrib/admin/static/admin/ /home/static/

python manage.py makemigrations
python manage.py migrate

uwsgi --wsgi-file "/home/HyperAnnales/wsgi.py" --http-socket 0.0.0.0:9090 --chdir "/home" --show-config

