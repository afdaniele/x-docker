ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

RUN mkdir -p /code

COPY ./ /code/

WORKDIR /code

RUN pip3 install /code/

CMD make test-unit
