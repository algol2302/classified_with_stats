# To run

virtualenv --python=/usr/bin/python3 .venv

source .venv/bin/activate

pip install -r requirements.txt

./docker/docker-compose up -d

env \`cat ./docker/.env\` python manage.py migrate

env \`cat ./docker/.env\` python manage.py createsuperuser

env \`cat ./docker/.env\` python manage.py runserver

Необходимо добавить пользователя: Anonymous

api: http://127.0.0.1:8000/api/v1/

frontend только начал делать, он не работает пока

В базе данных есть таблицы Просмотры (Объявлений) и Хиты (каждого объявления)

(git test)
