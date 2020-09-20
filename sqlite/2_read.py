import sqlite3

connection = sqlite3.connect("data.sqlite")
cursor = connection.cursor()

sql = "SELECT * FROM contacts WHERE name = 'Vasiliy'"

request_result = cursor.execute(sql)

for el in request_result:
    print(el)

connection.close()