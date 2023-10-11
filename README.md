# Docker-Djando-Postgress

1. Установить Doker и Docker-Compose

2. развернуть проект:

 docker-compose up -d

4. После того как проект развернется выполнить поочередно:

   docker exec -it django python manage.py migrate 
   
   docker exec -it django python manage.py makemigration
   
   docker exec -it django python manage.py createsuperuser
   
   docker exec -it django python manage.py migrate 
   
   docker exec -it django python manage.py makemigration 

 
 
 Что бы внести изменения в проект:
 
   docker-compose up -d --build web    

 доступ к ресурсам:
 
    localhost:8080        - джанго
    
    localhost:8080/admin  - админка джанго
    
    localhost:8081        - adminer

Остановить проект:

   docker-compose stop

Остановить проеект с удалением всех контейнеров:
  
   docker-compose down
