# A simple pet project to test ClickHouse with the simple Django application

1.
    ```
    poetry init
    poetry install
    ```

2. `./docker/docker-compose up -d`

3. 
   ```
   env `cat ./docker/.env` python manage.py migrate
   env `cat ./docker/.env` python manage.py createsuperuser`
   env `cat ./docker/.env` python manage.py runserver
   ```
4. Необходимо добавить пользователя: `Anonymous`

5. api: http://127.0.0.1:8000/api/v1/
