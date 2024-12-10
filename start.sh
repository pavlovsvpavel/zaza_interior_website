#!/bin/bash

echo "Migrating database..."
python manage.py makemigrations
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating locale files..."
python manage.py makemessages -l bg
python manage.py compilemessages

# Create superuser if it does not already exist
echo "Creating superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'qwer123456')
EOF

# Start Gunicorn
gunicorn --bind 0.0.0.0:10000 zaza_interior.wsgi:application &

# Start Nginx (this will run in the foreground)
nginx -g 'daemon off;'



