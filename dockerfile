FROM ubuntu:latest
FROM python:3.6.8

WORKDIR /usr/src/app

COPY . .

RUN apt update
RUN apt install -y graphviz
RUN pip3 install --upgrade pip
RUN pip3 install pillow


CMD ["python", "dijkstra.py"]