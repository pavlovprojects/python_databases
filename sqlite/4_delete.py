import sqlite3

connection = sqlite3.connect("data.sqlite")
cursor = connection.cursor()

# cursor.execute("DROP TABLE contacts;")
cursor.execute("DROP TABLE IF EXISTS contacts;")

# sql = "DELETE FROM contacts WHERE name = ?"
#
# cursor.execute(sql, ("HELLOTEST",))
# connection.commit()

connection.close()