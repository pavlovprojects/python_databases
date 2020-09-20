import sqlite3

connection = sqlite3.connect("db.sqlite")
cursor = connection.cursor()

with open("contacts.sql", "r") as script:
    cursor.execute(script.read())

sql = "INSERT INTO contacts (name, email, phone, address) VALUES (?, ?, ?, ?)"
data = ("One", "Two", "Three", "Four")

# https://docs.python.org/3.7/library/sqlite3.html

with connection:
    cursor.execute(sql, data)


connection.close()
