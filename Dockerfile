FROM ubuntu:latest
FROM python:3.9.4

# RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

VOLUME /app
COPY . . 

# VOLUME [ "/data" ]
RUN apt update
RUN apt install graphviz -y

RUN pip3 install matplotlib numpy graphviz pydot IPython networkx pillow

CMD ["python", "gsht.py"]
