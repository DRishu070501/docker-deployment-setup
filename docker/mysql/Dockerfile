FROM mysql:8.0.33

ENV MYSQL_DATABASE=${MYSQL_DATABASE}
ENV MYSQL_USER=${MYSQL_USER}
ENV MYSQL_PASSWORD=${MYSQL_PASSWORD}
ENV MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}

COPY docker/mysql/my.cnf /etc/mysql/conf.d/my.cnf
COPY ../../assets/init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
