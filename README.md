# Backend for TricksterTrust bank

----------------------

## Start:
- ### Переименуйте example.env → .env для считывания compose
```bash
mv example.env .env
```
- ### Заполните все поля в .env
```dotenv
# DATABASE
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_NAME=
SECRET_KEY=  # Django-secret-key

# REDIS
REDIS_PASSWORD=
REDIS_HOST=
REDIS_DATABASE=
```