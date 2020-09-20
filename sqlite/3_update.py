import sqlite3

connection = sqlite3.connect("data.sqlite")
cursor = connection.cursor()

# Bad example
sql = "UPDATE contacts SET address = 'TEST' WHERE name = 'Vasiliy'"

cursor.execute(sql)
connection.commit()

sql = "UPDATE contacts SET name = ? WHERE name = ?"
data = ("HELLOTEST", "Vasiliy")

cursor.execute(sql, data)
connection.commit()

connection.close()