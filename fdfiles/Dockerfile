FROM w251/cuda:dev-tx2-4.3_b132

ARG URL=http://169.44.201.108:7002/jetpacks/4.3

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    pkg-config \
    unzip \
    curl \
    cmake \
    git \
    python3-pip \
    python3-setuptools \
    python3-dev \
    python3 \
    mosquitto-clients \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /containerbase

RUN curl $URL/libopencv_3.3.1-2-g31ccdfe11_arm64.deb  -so libopencv_3.3.1-2-g31ccdfe11_arm64.deb
RUN curl $URL/libopencv-dev_3.3.1-2-g31ccdfe11_arm64.deb -so libopencv-dev_3.3.1-2-g31ccdfe11_arm64.deb
RUN curl $URL/libopencv-python_3.3.1-2-g31ccdfe11_arm64.deb -so libopencv-python_3.3.1-2-g31ccdfe11_arm64.deb

RUN apt remove -y libopencv-calib3d-dev libopencv-core-dev 

RUN apt install -y  libtbb-dev libavcodec-dev libavformat-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev 
# RUN apt install -y libgtk2.0-dev
RUN apt install -y libswscale-dev libv4l-dev
RUN dpkg -i *.deb

RUN apt install -y libcanberra-gtk-module libcanberra-gtk3-module libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev 

RUN pip3 install cython
RUN pip3 install numpy
# RUN pip3 install opencv-python
RUN pip3 install paho-mqtt
RUN pip3 install requests

RUN sed -i "s/^GPU=0/GPU=1/g" Makefile && sed -i "s/^CUDNN=0/CUDNN=1/g" Makefile && sed -i "s/^OPENCV=0/OPENCV=1/g" Makefile

ENV PATH $PATH:/usr/local/cuda-10.0/bin
RUN ldconfig
RUN make -j6
 
VOLUME /containerbase

# assumes that the root is /fdfiles
COPY . /containerbase

RUN rm -f /containerbase/*.deb

ENTRYPOINT python3 face_detector.py
