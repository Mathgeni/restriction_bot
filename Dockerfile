FROM python:3.12-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

RUN pip install poetry

COPY . .
RUN poetry config virtualenvs.in-project true && \
    poetry install --only=main --no-root

FROM base as final

COPY --from=builder /app/ ./
ENV PATH="/app/.venv/bin:$PATH"
