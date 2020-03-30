import psycopg2

connection = psycopg2.connect(database='contacts',
                              user='postgres',
                              password='root',
                              host='0.0.0.0',
                              port='3306')

cursor = connection.cursor()

# Выполняем запрос
cursor.execute("UPDATE contacts SET name='TEST' WHERE name='Vasya'")
connection.commit()

# Изменяем таблицу
cursor.execute("ALTER TABLE contacts DROP adress")
connection.commit()

# Закрываемся
cursor.close()
connection.close()
