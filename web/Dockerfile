FROM buildpack-deps:buster

COPY . /app

RUN apt-get update && apt-get install -y python-pip

WORKDIR /app

RUN pip install -r requirements.txt
