#!/bin/bash

cd /app/src/core/infrastructure/django

if [ ! -f wsgi.py ]; then
    echo "Error $(pwd)"
    exit 1
fi

exec gunicorn \
    --access-logfile - \
    --error-logfile - \
    --log-level debug \
    wsgi:application \
    --bind 0.0.0.0:8080 \
    --reload