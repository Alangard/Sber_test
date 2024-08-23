FROM python:3.11-slim

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock /code/

RUN poetry config virtualenvs.create false && poetry install --only main --no-interaction --no-ansi

COPY . /code/

EXPOSE 8000

# CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
