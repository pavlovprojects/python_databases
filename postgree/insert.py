import psycopg2

connection = psycopg2.connect(database='contacts', user='postgres', password='root', host='0.0.0.0', port='3306')
cursor = connection.cursor()

# Добавление одного кортежа данных
sql =  "INSERT INTO contacts (name, phone, email, adress) VALUES (%s, %s, %s, %s)"
values = ('Test1', '8999999', 'a@mail.ru', 'Moscow')
cursor.execute(sql, values)
connection.commit()

values = [
    ("Vasya000", "89009009999", None, "Moscow"),
    ("Vasya2", "89009009999", None, "Moscow"),
    ("Vasya3", "89009009999", None, "Moscow"),
    ("Vasya5", "89009009999", None, "Moscow"),
]

cursor.executemany(sql, values)
connection.commit()

cursor.close()
connection.close()
