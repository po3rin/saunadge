FROM python:3.9-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install poetry && \
	poetry config virtualenvs.create false && poetry install --no-dev

CMD exec  poetry run gunicorn --workers 1 --threads 8 --timeout 0 -b 0.0.0.0:8080 --log-level error saunadge.server:app
