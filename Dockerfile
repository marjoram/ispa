FROM python:3.5
ENV PYTHONUNBUFFERED 1

COPY requirements/base.txt /home/docker/requirements-base.txt
COPY requirements/prod.txt /home/docker/requirements-prod.txt

WORKDIR /home/docker/ispa

COPY gunicorn.sh /gunicorn.sh

RUN pip install --no-cache-dir -r /home/docker/requirements-base.txt\
      -r /home/docker/requirements-prod.txt

WORKDIR /home/docker/ispa

COPY gunicorn.sh /gunicorn.sh
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY migration.sh /migration.sh
RUN  chmod +x /gunicorn.sh && chmod +x /docker-entrypoint.sh \
    && chmod +x /migration.sh

COPY ispa/ .

ENTRYPOINT ["/docker-entrypoint.sh"]
