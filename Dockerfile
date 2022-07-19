FROM python:3.9.13-slim

ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

COPY  . .
COPY /requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt