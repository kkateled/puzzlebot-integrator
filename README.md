### Начальная установка окружения

```commandline
pip install poetry==1.6.1
poetry install
```

to make proper fastapi start initialise `.env` file, use `.env.template` for it.

### Создание среды миграции
- ```alembic init migrations```
- set env_variables on migrations\env.py
- create migration ```alembic revision -m 'create anymessage table'```
- launch migration ```alembic upgrade heads```

