FROM python:3.9.13-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY  . .
COPY /requirements.txt .
RUN pip install -r requirements.txt
