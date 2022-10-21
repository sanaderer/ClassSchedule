#!/bin/bash

python manage.py makemigrations
python manage.py migrate --run-syncdb

# generic way to autocreate superuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell

python3 manage.py runserver 0.0.0.0:8000
