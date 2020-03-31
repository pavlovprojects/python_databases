import sqlite3

connection = sqlite3.connect("db.sqlite")

sql = "INSERT INTO contacts (name, email, phone, address) VALUES (?, ?, ?, ?)"
data = ("One", "Two", "Three", "Four")

# https://docs.python.org/3.7/library/sqlite3.html

with connection:
    connection.execute(sql, data)
    # roll back automatically

connection.close()
