FROM python:3.9-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install poetry && \
	poetry install

EXPOSE 8000
ENTRYPOINT ["poetry", "run", "gunicorn", "-w", "1", "--bind", "0.0.0.0:8080", "saunadge.server:app"]
