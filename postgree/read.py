import psycopg2

connection = psycopg2.connect(database='contacts',
                              user='postgres',
                              password='root',
                              host='0.0.0.0',
                              port='3306')
cursor = connection.cursor()

# Выполняем запрос
cursor.execute("SELECT * FROM contacts")

# Получаем данные в виде кортежей
for row in cursor.fetchall():
    print(row)

# Закрываемся
cursor.close()
connection.close()