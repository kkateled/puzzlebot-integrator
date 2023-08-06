FROM python:3.9-alpine

RUN pip install poetry==1.5.1

WORKDIR /app

COPY poetry.lock .

COPY README.md .

COPY pyproject.toml .

RUN poetry config virtualenvs.create false

RUN poetry install --no-root

COPY . .

CMD [ "poetry", "run", "main.py" ]