web: gunicorn myapp.wsgi --log-file -
migrate: python manage.py migrate --settings=myapp.settings.production
seed: python manage.py loaddata myapp/item/fixtures/modi-items-data.json
seed: python manage.py loaddata myapp/item/fixtures/modi-ingred-data.json