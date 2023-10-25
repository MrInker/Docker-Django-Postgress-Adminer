# Docker-Djando-Postgress

1. Установить Doker и Docker-Compose

2. развернуть проект:

   docker-compose up -d

4. После того как проект развернется выполнить поочередно:

   docker exec -it django python manage.py makemigrations

   docker exec -it django python manage.py migrate 
   
   docker exec -it django python manage.py createsuperuser
   
   docker exec -it django python manage.py migrate 
   
   
 6. Перезапускаем сервис с джанго:

    docker-compose restart web

     
 
 Что бы внести изменения в проект:
 
   docker-compose up -d --build web    

 доступ к ресурсам:
 
    - localhost:8000        - джанго
    - localhost:8000/admin  - админка джанго
    - localhost:8001        - adminer

Остановить проект:

   docker-compose stop

Остановить проеект с удалением всех контейнеров:
  
   docker-compose down
