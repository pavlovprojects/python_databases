import sqlite3

connection = sqlite3.connect("db.sqlite")

with open("contacts.sql", "r") as script:
    connection.execute(script.read())

sql = "INSERT INTO contacts (name, email, phone, address) VALUES (?, ?, ?, ?)"
data = ("Vasiliy", "vasiliy@mail.ru", "+79160001234", "Moscow")
connection.execute(sql, data)
connection.commit()

# Множественное добавление
# all_data = [
#     ("Vasiliy1", "vasiliy@mail.ru", "+79160001234", "Moscow"),
#     ("Vasiliy2", "vasiliy@mail.ru", "+79160001234", "Moscow"),
#     ("Vasiliy3", "vasiliy@mail.ru", "+79160001234", "Moscow"),
#     ("Vasiliy4", "vasiliy@mail.ru", "+79160001234", "Moscow")
# ]
# connection.executemany(sql, all_data)
# connection.commit()

connection.close()
