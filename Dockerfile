FROM python:3.10-buster

RUN pip install poetry
ADD app /application
WORKDIR /application
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
CMD ["django", "manage.py", "runserver"]