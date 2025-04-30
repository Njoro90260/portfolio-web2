#!/bin/sh
set -e

echo "Entrypoint script running..."

# Validate secret key
if [ -z "$SECRET_KEY" ] || [ "$SECRET_KEY" = "default-dev-secret-key" ] || [ "$SECRET_KEY" = "must-be-set-for-production" ]; then
    echo "ERROR: SECRET_KEY must be properly configured"
    echo "For production, set it in your environment variables or .env.prod file"
    echo "For development, you can use the default in .env file"
    exit 1
fi

cd /app

# Wait for PostgreSQL
echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

if [ "$CREATE_SUPERUSER" = "true" ]; then
    echo "Creating superuser..."
    python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists():
    User.objects.create_superuser(
        username='${DJANGO_SUPERUSER_USERNAME}',
        email='${DJANGO_SUPERUSER_EMAIL}',
        password='${DJANGO_SUPERUSER_PASSWORD}'
    )
EOF
else
    echo "Superuser creation skipped."
fi

# Add to entrypoint.sh before starting uWSGI
echo "Verifying permissions..."
ls -la /app/vol
touch /app/vol/static/testfile && rm /app/vol/static/testfile && echo "Static files writable"
touch /app/vol/media/testfile && rm /app/vol/media/testfile && echo "Media files writable"
# Determine server type based on environment variable
if [ "$SERVER_TYPE" = "uwsgi" ]; then
    echo "Starting uWSGI server (development mode with uWSGI)..."
    uwsgi --http :8000 \
    --master \
    --enable-threads \
    --module portfolio.wsgi \
    --buffer-size 32768 \
    --http-timeout 300 \
    --static-safe /static=/app/vol/static \
    --static-safe /media=/app/vol/media \
    --processes 2 \
    --threads 2 \
    --harakiri 30 \
    --max-requests 500
else
    echo "Starting Gunicorn server (production mode)..."
    exec gunicorn portfolio.wsgi:application \
        --bind 0.0.0.0:8000 \
        --workers 4 \
        --worker-class sync \
        --timeout 120 \
        --log-level info \
        --access-logfile - \
        --error-logfile -
fi