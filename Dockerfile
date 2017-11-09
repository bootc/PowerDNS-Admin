FROM debian:stretch

LABEL summary="PowerDNS-Admin Web GUI" \
      io.k8s.description="A web interface for managing DNS records through PowerDNS." \
      io.k8s.display-name="PowerDNS-Admin" \
      license="MIT" \
      architecture="x86_64" \
      maintainer="Chris Boot <bootc@boo.tc>"

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install -y \
    libldap2-dev \
    libsasl2-dev \
    python-dev \
    python-mysqldb \
    python-pip \
    python-psycopg2 \
    uwsgi \
    uwsgi-plugin-python \
    && rm -rf /var/lib/apt/lists/* && \
    mkdir /code

WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

COPY config_template.py /code/config.py

EXPOSE 8080
CMD /usr/bin/uwsgi \
    --plugin python \
    --chdir /code \
    --master \
    --processes 2 \
    --threads 2 \
    --die-on-term \
    --http-socket :8080 \
    --wsgi-file /code/run.wsgi
