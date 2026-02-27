ARG PYTHON_VERSION=3.11.2-bullseye

#Copying or using the python version version above as a env variable
FROM python:${PYTHON_VERSION} as python   

FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=local

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev
COPY requirements/base.txt ./requirements.txt
RUN pip wheel --wheel-dir /usr/src/app/wheels -r requirements.txt

FROM python as python-runtime-stage
ARG BUILD_ENVIRONMENT=local

ARG APP_HOME=/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}
WORKDIR ${APP_HOME}
RUN apt-get update && apt-get install --no-install-recommends -y \
libpq-dev \
gettext \
&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
&& rm -rf /var/lib/apt/lists/*
COPY --from=python-build-stage /usr/src/app/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels /wheels/* \
&& rm  -rf /wheels/

COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint 
RUN chmod +x /entrypoint

#Service script
# We have 3 services: django, celery worker and celery flower. Each service has its own start script. We copy all 3 scripts to the image and make them executable. The entrypoint script will decide which start script to run based on the BUILD_ENV variable.
COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./docker/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower


# Copy the rest of the application code
COPY . ${APP_HOME}
ENTRYPOINT [ "/entrypoint" ]