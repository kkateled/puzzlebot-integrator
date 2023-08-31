FROM python:3.10-alpine

RUN pip install poetry==1.6.1

WORKDIR /app

COPY poetry.lock .
COPY README.md .
COPY pyproject.toml .

RUN poetry config virtualenvs.create false \
    && poetry install --no-root

COPY . .

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]