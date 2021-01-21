FROM python:3.9-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install poetry && \
	poetry config settings.virtualenvs.create false && \
	poetry install -n

EXPOSE 8000
ENTRYPOINT ["poetry","run","saunadge"]
