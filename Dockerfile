# use image of pytjon
FROM python:3.8-slim-buster

# show event 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# directory
WORKDIR /app

# we need install app for image
COPY requirements.txt /app/

# install requirements.txt 
RUN pip install --upgrade pip 
RUN pip install  -r requirements.txt

# copy directory to image
COPY ./core /app/

# when we have a docker- compose this option is off 
# CMD [ "python3", "manage.py","runserver","0.0.0.0:8000" ]

# when we use without docker-compose.yml
# make  this file to terminal
# docker build -t django 
# run this action
# docker run -p 8000:800 django 