#!/bin/bash

# If we don't have a database, migrate one
if [ -z "$BREW_DB" ]; then
    python manage.py migrate
fi

/usr/local/bin/gunicorn --bind 0.0.0.0:80 \
                        --error-logfile - \
                        brewwolf.wsgi:application