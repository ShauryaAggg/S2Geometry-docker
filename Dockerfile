ARG BUILDPLATFORM=linux/amd64
FROM --platform=$BUILDPLATFORM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y \
    git \
    swig \
    cmake \
    cython \
    proj-bin \
    proj-data \
    libssl-dev \
    libproj-dev \
    libgeos-dev \
    python3-dev \
    python3-pip \
    libgtest-dev \
    libgflags-dev \
    build-essential \
    libgoogle-glog-dev 

# Symbolic link to use python3 as default
RUN ln -sf /usr/bin/python3 /usr/bin/python

ENV s2tag=v0.9.0
# Use v0.9.0 tags for build
RUN git clone -b ${s2tag} https://github.com/google/s2geometry.git

WORKDIR /s2geometry/

RUN git submodule add https://github.com/abseil/abseil-cpp.git

## Build Abseil
RUN mkdir /s2geometry/abseil-cpp/build && \
    cd /s2geometry/abseil-cpp/build && \
    cmake .. \
    -DCMAKE_CXX_STANDARD=17 \
    -DABSL_ENABLE_INSTALL=ON \
    -DCMAKE_INSTALL_PREFIX=install/ \
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON && \
    cmake --build . && \
    cmake --build . --target install

RUN mkdir /s2geometry/build && \
    cd /s2geometry/build && \
    cmake .. \
    -DWITH_PYTHON=ON \
    -DCMAKE_CXX_STANDARD=17 \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib/x86_64-linux-gnu \
    -DCMAKE_PREFIX_PATH=abseil-cpp/build/install/ \
    -DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3.6 && \
    make install

## A hack so that _pywraps2.so will recognize libs2.so 
RUN cp /usr/local/lib/libs2.so /usr/lib/x86_64-linux-gnu

RUN pip3 install jupyter \
    numpy \
    scipy \
    pandas \
    shapely \
    pykdtree \
    matplotlib \
    ipywidgets \
    Pillow==6.2.2

RUN pip3 install Cartopy

WORKDIR /usr/src/notebooks/
COPY ./notebooks/ /usr/src/notebooks/

EXPOSE 8888
CMD [ "jupyter", "notebook", "--ip", "0.0.0.0", "--port", "8888",  "--no-browser", "--allow-root" ]