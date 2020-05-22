# Доска объявлений на MongoDb

* Clone the repo
* from the repo dir:
1. Запустить контейнер mongo:
* docker run --name mongo-instance --rm -d -p "27017:27017" mongo:4.2.3
2. Запустить контейнер redis:
* docker run --name redis-instance --rm -d -p 6379:6379 redis:5.0.7 redis-server --appendonly yes
3. Запустить приложение на Django:
* python manage.py runserver 

# NB! Pymongo==3.7.2

Эндпоинты:
* GET все статьи: http://127.0.0.1:8000/
* POST добавить статью: http://127.0.0.1:8000/add/message/
* POST добавить комментарий: http://127.0.0.1:8000/add/comment/
* POST добавить тэг: http://127.0.0.1:8000/add/tag/
* GET детализированное сообщение о статье http://127.0.0.1:8000/message/<message:id:>
* GET статистика по статье: http://127.0.0.1:8000/stats/<message:id:>
