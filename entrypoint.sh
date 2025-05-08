#!/bin/sh
set -e

# Configurable defaults
WORKERS=${GUNICORN_WORKERS:-$((2 * $(nproc) + 1))}
TIMEOUT=${GUNICORN_TIMEOUT:-120}

# Skip if flag exists
if [ -n "$SKIP_ENTRYPOINT" ]; then
  exec "$@"
  exit 0
fi

# Django setup
echo "----- Running migrations -----"
python manage.py makemigrations --no-input

echo "----- Running migrate -----"
python manage.py migrate --no-input

echo "----- Collecting static files -----"
python manage.py collectstatic --no-input

echo "----- Compile translations django.po file -----"
python manage.py compilemessages

# Start server
echo "----- Starting Gunicorn with $WORKERS workers (timeout: $TIMEOUT) -----"
exec gunicorn zaza_interior.wsgi:application \
    --bind=0.0.0.0:8000 \
    --workers="$WORKERS" \
    --timeout="$TIMEOUT" \
    --access-logfile - \
    --error-logfile -
