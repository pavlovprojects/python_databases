# Step-by-Step guide for mysql docker setup

# docker run -e POSTGRES_PASSWORD=root -p 3306:5432 -d postgres
# docker exec -it {CONTAINER_ID} bash
# psql -U postgres
# Enter password: {PASSWORD}
# \list - show databases
# \c {database_name}
# show databases; show tables;
# drop database; drop table;

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


connection = psycopg2.connect(database='contacts',
                              user='postgres',
                              password='root',
                              host='0.0.0.0',
                              port='3306')

connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()

try:
    with open("contacts_table.sql", "r") as script:
        cursor.execute(script.read())
except psycopg2.errors.DuplicateTable as e:
    print(e)

cursor.close()
connection.close()
