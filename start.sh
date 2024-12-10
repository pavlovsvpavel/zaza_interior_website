#!/bin/bash

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn and Nginx
gunicorn --bind 0.0.0.0:8000 zaza_interior.wsgi &
exec nginx -g 'daemon off;'

