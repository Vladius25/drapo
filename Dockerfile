FROM python:3.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /drapo
WORKDIR /drapo

COPY src/web/requirements.txt /drapo/
RUN pip install -r requirements.txt
COPY src/web/ /drapo/

RUN python manage.py migrate
