FROM python:3.10.8-alpine

WORKDIR '/opt'

RUN pip install --upgrade pip --no-cache-dir && pip install poetry==1.2.0 --no-cache-dir
RUN apk update && apk add make

COPY poetry.lock pyproject.toml README.md ./
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-root --no-cache

COPY traceback_stats ./traceback_stats
RUN poetry build -f wheel
RUN pip install dist/*.whl --no-deps --no-cache-dir
RUN rm -r *

COPY makefile ./

ENTRYPOINT gunicorn traceback_stats.traceback_stats.wsgi --workers 1 --bind 0.0.0.0:8080