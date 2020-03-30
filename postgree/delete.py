import mysql.connector

connection = mysql.connector.connect(database='contacts', user='root', password='root', host='0.0.0.0', port='3306')
cursor = connection.cursor()

# Выполняем запрос
cursor.execute("DELETE FROM contacts WHERE name='Test'")
connection.commit()

# Закрываемся
cursor.close()
connection.close()