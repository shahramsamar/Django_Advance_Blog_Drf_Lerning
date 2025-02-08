
# general commands:

# check run container
  docker ps -a

# show images
 docker image 

# remove 
 docker rmi name or id 



# ready django in root and requirements.txt
# create  image 
 docker bulid -t django .


# run image and project
 docker run -p 8000:8000 django



# when we use to docker-compose.yml file 

## create automatic  in vscode for developer
# first create  project in django 
# second press f1  and choses add docker file to workspace 
# third choses for your app like this python django 
# forth choses manage.py 
# fifth choses your opinion port like: 8000
# sixth are you want to include optional docker compose file   press: yes 
# finish

# use automatic docker file 
# use -f for manual docker-compose
 docker-compose -f docker-compose.yml up --build




# create docker-compose.yml file 

# run docker compose for project 
 docker-compose up --build -d
 docker-compose up --build
 docker-compose up 

# show logs 
 docker-compose logs -f 

exec backend sh -c '


# when we have create app in container 
 docker-compose exec backend sh -c "python manage.py startapp blog" 


# package in docker install
docker-compose exec name container(backend) sh -c "pip install  package name " 
docker-compose exec name container(backend) sh -c "pip install Django==4.2.7"  ? 
docker-compose exec backend sh -c "python manage.py makemigrations"
docker-compose exec backend sh -c "python manage.py migrate"
docker-compose exec backend sh -c "python manage.py collectstatic"

docker-compose exec backend sh -c "python manage.py createsuperuser"
docker-compose exec backend sh -c "python manage.py changepassword username or email"

 # djangorestframework
 docker-compose exec backend sh -c "pip install djangorestframework"
 docker-compose exec backend sh -c "pip install markdown"
 docker-compose exec backend sh -c "pip install django-filter"
 docker-compose exec backend sh -c "pip install djangorestframework-simplejwt"
 docker-compose exec backend sh -c "pip install django-mail-templated"

docker-compose exec backend sh -c "pip install -U djoser"
docker-compose exec backend sh -c "pip install pytest"
docker-compose exec backend sh -c "pip install django-pytest"

# coreapi
docker-compose exec backend sh -c "pip install coreapi"

# refactoring and test 
docker-compose exec backend sh -c "pip install black"
docker-compose exec backend sh -c "pip install flake8-django"