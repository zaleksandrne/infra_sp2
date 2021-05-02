# API_YamDB
### Описание
API для Yatube - сервиса для хранения краткого описания 
литеретурных произведений и обмена отзывами на них
### Технологии
Postgres 12.4
Docker Compose 3.8
Python 3.8.5
Django 3.0.5
Django REST framework 3.11.0
### Запуск проекта в Docker Compose
- Соберите и запустите контейнеры
```
docker-compose up -d --build 
``` 
- Выполните миграции
```
docker-compose exec web python manage.py migrate --noinput
```
- Создайте суперпользователя
```
docker-compose exec web python manage.py createsuperuser
```
- Соберите статические файлы
```
docker-compose exec web python manage.py collectstatic --no-input 
```
- Для загрузки тестовых данных перенисите данные из дампа
```
docker-compose exec web python manage.py loaddata fixtures.json 
```

