FROM python:3

ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get upgrade -y && \
    pip install --upgrade pip && \
    pip install Cython

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
