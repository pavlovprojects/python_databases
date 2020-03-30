# Step-by-Step guide for mysql docker setup

# use docker mysql/mysql-server
# docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD={PASSWORD} -e MYSQL_ROOT_HOST=% mysql/mysql-server
# docker exec -it {CONTAINER_ID} bash
# bash-4.2# mysql -p
# Enter password: {PASSWORD}
# create database contacts;
# connect {database_name}
# show databases; show tables;
# drop database; drop table;

DB_NAME = 'contacts'
TABLE = 'contacts'

import mysql.connector

connection = mysql.connector.connect(user='root', password='root', host='0.0.0.0', port='3306')
cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))

cursor.execute("USE {}".format(DB_NAME))

with open("contacts_table.sql", "r") as script:
    cursor.execute(script.read())


# # Добавление одного кортежа данных
# sql = "INSERT INTO contacts (name, phone, email, adress) VALUES (%s, %s, %s, %s)"
# values = ("Vasya1", "89009009999", None, "Moscow")
# cursor.execute(sql, values)
# connection.commit()


# # Множественное обавление
# values = [
#     ("Vasya000", "89009009999", None, "Moscow"),
#     ("Vasya2", "89009009999", None, "Moscow"),
#     ("Vasya3", "89009009999", None, "Moscow"),
#     ("Vasya5", "89009009999", None, "Moscow"),
# ]
# sql = "INSERT INTO contacts (name, phone, email, adress) VALUES (%s, %s, %s, %s)"
#
# cursor.executemany(sql, values)
# connection.commit()

cursor.close()
connection.close()
