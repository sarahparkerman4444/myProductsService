#!/bin/bash

set -e

bash scripts/tcp-port-wait.sh $DATABASE_HOST $DATABASE_PORT

python manage.py migrate

gunicorn products_service.wsgi --config products_service/gunicorn_conf.py
