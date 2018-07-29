FROM python:3.7-stretch
RUN mkdir /code
WORKDIR /code
COPY . /code

RUN pip install -r requirements.txt

RUN pytest
