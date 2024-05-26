FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt auto-remove -y

WORKDIR /app
COPY requirements.tf.txt .

RUN /bin/sh -c "pip install -r requirements.tf.txt"

COPY . .