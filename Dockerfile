FROM python:3.6
WORKDIR /mnt/scripts/
RUN pip install requests
RUN pip install telegram-send
RUN pip install SQLAlchemy
RUN apt-get update && \
    apt-get install -y postgresql-client

RUN pip install sqlalchemy
RUN pip install geoalchemy2
RUN pip install sqlalchemy-utils
RUN pip install psycopg2-binary
RUN apt-get -y  install libpq-dev 
RUN pip install psycopg2 
RUN pip install redshift-sqlalchemy 
RUN pip install sqlparse

RUN pip install matplotlib
# COPY . .
# RUN python setup.py install
# RUN python -m unittest
# ENTRYPOINT ["tri_ad"]
