FROM ubuntu:latest
FROM python:3.6.8

WORKDIR /usr/src/app

COPY . .

RUN apt update
RUN apt install graphviz 
RUN pip3 install sys os PIL

CMD ["python", "dijkstra.py"]