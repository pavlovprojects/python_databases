import sqlite3

connection = sqlite3.connect("db.sqlite")

sql = "DELETE FROM contacts WHERE name = ?"

connection.execute(sql, ("TEST",))

# connection.commit()

connection.close()