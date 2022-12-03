FROM python:3.10.8-alpine as build

WORKDIR '/opt'
RUN pip install poetry
COPY . .
RUN poetry build -f wheel

FROM python:3.10.8-alpine

WORKDIR '/opt'

COPY --from=build /opt/dist/* ./

RUN pip install *.whl && rm *.whl

ENTRYPOINT gunicorn traceback_stats.traceback_stats.wsgi --workers 1 --bind 0.0.0.0:8080