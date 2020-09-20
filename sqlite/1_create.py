import sqlite3

connection = sqlite3.connect("data.sqlite")
cursor = connection.cursor()

with open("contacts.sql", "r") as script:
    cursor.execute(script.read())

sql = "INSERT INTO contacts (name, email, phone, address) VALUES (?, ?, ?, ?)"
data = ("Vasiliy", "vasiliy@mail.ru", "+79160001234", "Moscow")

cursor.execute(sql, data)

# Commit can be called only from connection!
connection.commit()

all_data = [
    ("Vasiliy1", "vasiliy@mail.ru", "+79160001234", "Moscow"),
    ("Vasiliy2", "vasiliy@mail.ru", "+79160001234", "Moscow"),
    ("Vasiliy3", "vasiliy@mail.ru", "+79160001234", "Moscow"),
    ("Vasiliy4", "vasiliy@mail.ru", "+79160001234", "Moscow")
]

cursor.executemany(sql, all_data)

connection.commit()

connection.close()
