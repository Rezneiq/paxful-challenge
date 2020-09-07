
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev  -y