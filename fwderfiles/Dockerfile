FROM ubuntu:bionic
USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    cmake \
    git \
    python3-pip \
    python3-setuptools \
    python3-dev \
    python3 \
    mosquitto-clients \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install paho-mqtt
RUN pip3 install requests
RUN mkdir /data

VOLUME /tmp
WORKDIR /tmp

# assumes that the root is /fwderfiles
COPY . /tmp

ENTRYPOINT python3 fwder.py
