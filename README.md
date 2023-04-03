# Backend for TricksterTrust bank

![python-version](https://img.shields.io/badge/python-3.10-blue.svg)
![django-version](https://img.shields.io/badge/django-4.1.7-orange/)
----------------------

### Полноценное ядро для банковского приложения написанное с применением `Django REST Api`, `Celery`

### Возможности проекта:

- [x] Полноценный playground проекта, реализующий функционал swagger со стороны backend `/dev/methods/`
- [x] Получение курса валют, а так же возможность обменять одну валюту в другую
- [x] Автоматическое обновление валют
- [ ] JWT авторизация
- [ ] websocket бот с применением chatgpt
- [ ] общий функционал банковского приложения

## Installation:

- ### Установите проект локально

```bash
git clone https://github.com/TricksterTrust/backend
```

- ### Переименуйте example.env → .env для считывания compose

```bash
mv example.env .env
```

- ### Заполните все поля в .env

| Parameter           | Description                                               |
|---------------------|-----------------------------------------------------------|
| `POSTGRES_USER`     | Имя пользователя для postgres контейнера в docker-compose |
| `POSTGRES_PASSWORD` | Пароль для контейнера                                     |
| `POSTGRES_HOST`     | Название postgres контейнера                              |
| `POSTGRES_NAME`     | Название таблицы                                          |
| `SECRET_KEY`        | Django-ключ доступа                                       |
| `REDIS_PASSWORD`    | Пароль для доступа к хранилищу redis                      |
| `REDIS_HOST`        | Название redis контейнера                                 |
| `REDIS_DATABASE`    | База данных redis (обычно 0)                              |
| `BACKEND_PORT`      | Порт, по которому backend будет ждать подключения         |

## Required

- #### Python 3.10+
- #### OpenAI token

## Install

- #### Установите docker-compose

```bash
docker-compose up -d
```