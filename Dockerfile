FROM python:3

FROM python:3
USER app
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN chown app:app -R /code

WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
