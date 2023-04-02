FROM python:3.10-buster

RUN pip install poetry
ADD app /application
WORKDIR /application/TrickerTrust
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
ADD entrypoint.sh /application/TrickerTrust
RUN ["chmod", "+x", "/application/TrickerTrust/entrypoint.sh"]
ENTRYPOINT ["/application/TrickerTrust/entrypoint.sh"]