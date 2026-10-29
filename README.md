# Docker-Django-PostgreSQL

Пример Django-проекта (Django 5.2 LTS) с PostgreSQL, разворачиваемый через Docker Compose.

## Требования

- Docker и Docker Compose (для сборки через контейнеры), **или**
- Python 3.12+ и сервер PostgreSQL 14+ (для локального запуска)

## Зависимости (`requirements.txt`)

| Пакет       | Версия  | Назначение                          |
|-------------|---------|-------------------------------------|
| Django      | 5.2.18  | Фреймворк (LTS, поддержка до 2028)  |
| psycopg2    | 2.9.13  | Драйвер PostgreSQL                  |
| sqlparse    | 0.6.0   | Парсинг SQL (зависимость Django)    |
| asgiref     | 3.13.0  | ASGI-утилиты (зависимость Django)   |

## Сборка и запуск через Docker

```bash
docker compose up -d --build
```

После развертывания выполнить поочередно:

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Перезапуск сервиса Django после изменений:

```bash
docker compose restart web
```

Приложение доступно на http://localhost:8000 , админка — http://localhost:8000/admin

## Локальная сборка (без Docker)

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Поднять PostgreSQL (если нет локального сервера):
docker run -d --name pg -e POSTGRES_DB=postgres -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres:17

export POSTGRES_NAME=postgres POSTGRES_USER=postgres POSTGRES_PASSWORD=postgres POSTGRES_HOST=localhost
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Переменные окружения

| Переменная           | По умолчанию | Описание                              |
|----------------------|--------------|---------------------------------------|
| POSTGRES_DB          | postgres     | Имя базы данных                       |
| POSTGRES_USER        | postgres     | Пользователь БД                       |
| POSTGRES_PASSWORD    | postgres     | Пароль БД                             |
| POSTGRES_HOST        | db           | Хост БД (в compose — сервис `db`)     |
| POSTGRES_PORT        | 5432         | Порт БД                               |
| DEBUG                | True         | Режим отладки (для прода — False)     |
| ALLOWED_HOSTS        | *            | Разрешенные хосты, через запятую      |
| CSRF_TRUSTED_ORIGINS | localhost:8000 | Доверенные origin для CSRF          |

## Структура проекта

```
config/               # настройки проекта (settings.py, urls.py, wsgi/asgi)
models/               # приложение: модели (models/MainModel.py), admin, views
models/migrations/    # миграции БД (0001_initial — модель MainProject)
Dockerfile            # образ: python:3.12-slim + gcc/libpq-dev для psycopg2
docker-compose.yml    # сервисы: web (Django :8000) + db (PostgreSQL :5432)
manage.py             # CLI Django
```

## Частые проблемы

- **Порт 5432 занят** — измените порт в `docker-compose.yml` или остановите локальный PostgreSQL.
- **Ошибка сборки psycopg2** — в образе уже установлены `gcc` и `libpq-dev`; при локальной сборке: `apt install gcc libpq-dev` (Debian/Ubuntu) / `brew install libpq` (macOS).
- **`Relational database does not exist`** — проверьте `POSTGRES_*` переменные и что сервис `db` поднялся (`docker compose ps`).
