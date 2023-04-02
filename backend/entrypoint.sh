#!/bin/bash
python manage.py makemigrations
python manage.py migrate

celery -A core.celery.app multi start worker --beat --logfile="$HOME/log/celery/%n%I.log" --pidfile="$HOME/run/celery/%n.pid"

python manage.py runserver 0.0.0.0:8000
