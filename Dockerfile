ARG PYTHON_VERSION=latest
FROM python:${PYTHON_VERSION}

RUN apt-get update && apt-get install -y zip
WORKDIR /nycduckdb/src
COPY ./src/ /nycduckdb/src/
RUN pip install pytest
RUN pip install -e .
ENTRYPOINT [ "python", "-m", "nycduckdb.cli" ]
CMD [ "--list-datasets" ]