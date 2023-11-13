# Note regarding python-alpine:
# https://dev.to/pmutua/the-best-docker-base-image-for-your-python-application-3o83
FROM python:3.11.6-slim

WORKDIR /web

RUN pip install poetry

COPY . /web

RUN POETRY_VIRTUALENVS_CREATE=false poetry install

VOLUME ["/web"]
