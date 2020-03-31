import sqlite3

connection = sqlite3.connect("db.sqlite")

sql = "UPDATE contacts SET name = 'TEST' WHERE name = 'Vasya'"

connection.execute(sql)

# connection.commit()

sql = "UPDATE contacts SET email = 'new_email2' WHERE email = 'new_email'"

connection.execute(sql)

# connection.commit()

connection.close()