import mysql.connector

connection = mysql.connector.connect(user='root', password='root', host='0.0.0.0', port='3306')

cursor = connection.cursor()

# Выбираем базу данных
cursor.execute("USE contacts")

# Выполняем запрос
cursor.execute("SELECT * FROM contacts")

# Получаем данные в виде кортежей
for row in cursor.fetchall():
    print(row)

# Закрываемся
cursor.close()
connection.close()
