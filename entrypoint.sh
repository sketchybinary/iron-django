#!/bin/bash

/usr/local/bin/gunicorn --bind 0.0.0.0:80 \
                        --error-logfile - \
                        brewwolf.wsgi:application