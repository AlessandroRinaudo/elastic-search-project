FROM python:3.9

WORKDIR /sds

RUN pip install requests

COPY ./samplaDataScript .
