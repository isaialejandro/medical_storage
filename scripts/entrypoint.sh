#!bin/sh


set -e

python3 manage.py collectstatic --noinput

uwsgi --socket :80 --master --enable-threads --module medical_storage.wsgi #runs app in uwsgi