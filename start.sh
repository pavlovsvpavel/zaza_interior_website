#!/bin/bash

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn and Nginx..."
gunicorn --bind 127.0.0.1:8000 zaza_interior.wsgi & exec nginx -g 'daemon off;'


