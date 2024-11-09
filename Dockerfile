FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y apt-utils gettext libpq-dev gcc && \
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

