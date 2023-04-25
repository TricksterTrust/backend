#!/bin/bash
python manage.py makemigrations
python manage.py migrate

celery -A core.celery.app multi start worker --beat --logfile="$HOME/log/celery/%n%I.log" --pidfile="$HOME/run/celery/%n.pid"
# celery -A core.celery.app worker -B -l debug
daphne -b 0.0.0.0 -p 8000 core.asgi:application
