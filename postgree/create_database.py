# Step-by-Step guide for mysql docker setup

# docker run -e POSTGRES_PASSWORD=root -p 3306:5432 -d postgres
# docker exec -it {CONTAINER_ID} bash
# psql -U postgres
# Enter password: {PASSWORD}
# \list - show databases
# \c {database_name}
# show databases; show tables;
# drop database; drop table;

DB_NAME = 'contacts'

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = psycopg2.connect(user='postgres', password='root', host='0.0.0.0', port='3306')
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()

try:
    create_database = "CREATE DATABASE {};".format(DB_NAME)
    cursor.execute(create_database)
except psycopg2.errors.DuplicateDatabase as e:
    print(e)

cursor.close()
connection.close()
