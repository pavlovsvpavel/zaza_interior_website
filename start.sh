#!/bin/bash

echo "Migrating database..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating locale files..."
python manage.py makemessages -l bg
python manage.py compilemessages

echo "Starting Gunicorn and Nginx..."
gunicorn --bind 0.0.0.0:10000 --access-logfile - --error-logfile - zaza_interior.wsgi:application & nginx -g 'daemon off;'



