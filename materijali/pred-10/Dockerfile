FROM python:3.9

# Install poetry
RUN pip install poetry

# Configure Poetry for deployment: no interaction, install packages directly (not in virtualenv)
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false

# Launch our celery project when Docker container starts
ENTRYPOINT ["celery", "--app=distributed.app", "worker", "--events", "--loglevel=INFO"]

# Setup our celery project working directory
WORKDIR /app

# Install our celery project, in production mode
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-dev
