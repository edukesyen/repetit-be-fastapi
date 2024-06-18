# Dockerfile
# Uses multi-stage builds requiring Docker 17.05 or higher
# See https://docs.docker.com/develop/develop-images/multistage-build/

# Creating a python base with shared environment variables
FROM python:3.10-slim as python-base

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
ENV PDM_HOME="/opt/pdm"
ENV PDM_VIRTUALENVS_IN_PROJECT=true
ENV PDM_NO_INTERACTION=1
ENV PYSETUP_PATH="/opt/pysetup"
ENV VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$PDM_HOME/bin:$VENV_PATH/bin:$PATH"


# builder-base is used to build dependencies
FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential

# Install PDM - respects $PDM_VERSION & $PDM_HOME
ENV PDM_VERSION=2.12.1
WORKDIR $PYSETUP_PATH
RUN curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python
RUN pdm venv create --name prod 3.10
# We copy our Python requirements here to cache them
# and install only runtime deps using pdm
WORKDIR $PYSETUP_PATH
COPY ./pdm.lock ./pyproject.toml ./
# RUN pdm use -f $VENV_PATH
RUN pdm venv activate prod
RUN pdm install --prod


# 'development' stage installs all dev deps and can be used to develop code.
# For example using docker-compose to mount local volume under /app
FROM python-base as production

# Copying poetry and venv into image
COPY --from=builder-base $PDM_HOME $PDM_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# venv already has runtime deps installed we get a quicker install
WORKDIR $PYSETUP_PATH
RUN pdm sync

COPY ./app /opt/code/app
WORKDIR /opt/code
COPY ./.env ./.env

EXPOSE 8000
# ENTRYPOINT ["./boot.sh"]
CMD ["exec", "gunicorn", "app.main:app", "-w", "1", "-b", "0.0.0.0", "--worker-class", "uvicorn.workers.UvicornWorker"]
