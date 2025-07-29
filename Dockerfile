FROM python:3.13-alpine AS builder

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    libpq-dev \
    zlib-dev \
    curl \
    && rm -rf /var/cache/apk/*

RUN pip install --no-cache-dir pipenv

COPY Pipfile Pipfile.lock /usr/src/web/

WORKDIR /usr/src/web

RUN pipenv install --deploy --ignore-pipfile && \
    pipenv requirements > requirements.txt && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/web/wheels -r requirements.txt

FROM python:3.13-alpine

RUN apk add --no-cache \
    libpq \
    libffi \
    zlib \
    && rm -rf /var/cache/apk/*

ADD . /app
WORKDIR /app/src
ENV PYTHONPATH=/app/src

COPY --from=builder /usr/src/web/wheels /wheels
COPY --from=builder /usr/src/web/requirements.txt /app/

RUN pip install --no-cache-dir /wheels/*

RUN chmod +x /app/entrypoints/test-django-entrypoint.sh
# CMD ["tail", "-f", "/dev/null"]
