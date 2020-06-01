FROM ubuntu
USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    cmake \
    git \
    python-pip \
    python-setuptools \
    python-dev \
    python3 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install numpy
RUN pip install opencv-python

VOLUME /containerbase
WORKDIR /containerbase

# assumes that the root is /fdfiles
COPY . /containerbase

ENTRYPOINT python3 face_detector.py
