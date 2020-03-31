import sqlite3

connection = sqlite3.connect("db.sqlite")

sql = "SELECT * FROM contacts WHERE name = 'Vasiliy'"

r = connection.execute(sql)

print(r.fetchone())

connection.close()