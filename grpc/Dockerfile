FROM python:3.12-slim

RUN apt update  && apt -y install curl

WORKDIR /src

COPY pyproject.toml poetry.lock /src/

RUN curl -sSL https://install.python-poetry.org | python3 - \
  && /root/.local/bin/poetry config virtualenvs.create false \
  && /root/.local/bin/poetry install --no-dev --no-interaction
