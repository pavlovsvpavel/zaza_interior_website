#FROM python:3.11-slim
#
#ENV DEBIAN_FRONTEND=noninteractive
#
#RUN apt-get update -y && \
#    apt-get upgrade -y && \
#    apt-get install -y apt-utils gettext libpq-dev gcc && \
#    apt-get clean && rm -rf /var/lib/apt/lists/*
#
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
#ENV HOME=/home/app
#ENV APP_HOME=/home/app/web
#
#WORKDIR $APP_HOME
#
#COPY ./requirements.txt .
#
#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
#
#COPY . .

# Use an official Python runtime as a parent image
FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y apt-utils gettext libpq-dev gcc && \
    apt-get install -y nginx && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

WORKDIR $APP_HOME

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# Copy Nginx configuration
COPY nginx/render/conf.d/web.conf /etc/nginx/render/conf.d/web.conf

COPY start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/bin/bash", "/start.sh"]
