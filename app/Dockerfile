FROM python:3

RUN apt-get update && apt-get upgrade

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

WORKDIR /app

EXPOSE 8000
