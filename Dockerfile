FROM python:3.6

RUN apt-get update \
    && apt-get install -y vim unzip \
    && pip install -U pip \
    && apt-get autoremove \
    && apt-get clean

RUN curl -sLO https://dl.google.com/go/go1.9.2.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.9.2.linux-amd64.tar.gz
ENV PATH $PATH:/usr/local/go/bin

ENV PROTOBUF_VERSION 3.5.1
RUN curl -sLO https://github.com/google/protobuf/releases/download/v${PROTOBUF_VERSION}/protoc-${PROTOBUF_VERSION}-linux-x86_64.zip \
    && unzip protoc-${PROTOBUF_VERSION}-linux-x86_64.zip -d ./usr/local \
    && chmod +x /usr/local/bin/protoc \
    && rm protoc-${PROTOBUF_VERSION}-linux-x86_64.zip

RUN go get github.com/gogo/protobuf/protoc-gen-gofast

ENV PYTHONUNBUFFERED 0

ENV TENDERMINT_PORT 46657

RUN mkdir -p /usr/src/app
COPY . /usr/src/app/
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -e .
