#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model

User = get_user_model()  # get the currently active user model,

User.objects.filter(username='$ADMIN_USER').exists() or \
    User.objects.create_superuser('$ADMIN_USER', '$ADMIN_USER_EMAIL', '$ADMIN_USER_PASSWORD')
EOF

exec "$@"
