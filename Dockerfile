FROM alpine:3.7

ARG BUILD_DATE=1970-01-01T00:00:00Z
ARG VCS_REF=

LABEL org.label-schema.vendor="Chris Boot" \
      org.label-schema.url="https://git.boo.tc/bootc/PowerDNS-Admin" \
      org.label-schema.name="PowerDNS-Admin" \
      org.label-schema.description="A web interface for managing DNS records through PowerDNS" \
      org.label-schema.license="MIT" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.build-date="${BUILD_DATE}" \
      org.label-schema.vcs-ref="${VCS_REF}" \
      org.label-schema.vcs-url="https://git.boo.tc/bootc/PowerDNS-Admin.git"

RUN apk add --no-cache --update \
        curl \
        python \
        py-mysqldb \
        py2-asn1 \
        py2-asn1-modules \
        py2-bcrypt \
        py2-cffi \
        py2-configobj \
        py2-decorator \
        py2-dnspython \
        py2-flask \
        py2-flask-oauthlib \
        py2-flask-wtf \
        py2-gunicorn \
        py2-pbr \
        py2-pip \
        py2-psycopg2 \
        py2-pyldap \
        py2-pysqlite \
        py2-requests \
        py2-six \
        py2-sqlalchemy \
        py2-sqlparse \
        py2-tempita \
    && rm -rf /var/cache/apk/*

WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt --upgrade-strategy only-if-needed

COPY config_docker.py /code/config.py

EXPOSE 8080
CMD /usr/bin/gunicorn \
    -b 0.0.0.0:8080 \
    --access-logfile - \
    app:app
