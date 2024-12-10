#!/bin/bash

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn and Nginx..."
gunicorn --bind 0.0.0.0:10000 --access-logfile - --error-logfile - zaza_interior.wsgi & nginx -g 'daemon off;'



