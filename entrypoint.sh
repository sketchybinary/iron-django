#!/bin/bash

cd /opt/
/usr/local/bin/gunicorn --bind 0.0.0.0:80 brewwolf.wsgi:application