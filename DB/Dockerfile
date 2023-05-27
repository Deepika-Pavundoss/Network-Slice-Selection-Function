FROM mysql:latest
ENV MYSQL_DATABASE=nssf \
    MYSQL_ROOT_PASSWORD=password \
    MYSQL_ROOT_HOST=% \
    MYSQL_ROOT_DB=root
ADD init.sql /docker-entrypoint-initdb.d
EXPOSE 3306
