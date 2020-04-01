# Занятие «Работа с СУБД»

## Вводная часть

**DB** (Database) - База данных, объем информации представленный в определенной структурированной форме таким образом, чтобы эти данные могли быть обработаны ЭВМ.

**SQL** (Structured Query Language) - Язык стуктурированных запросов, декларативный язык программирования, применяемый для создания, модификации и управления данными в реляционной базе данных, управляемой соответствующей системой управления базами данных..

**DBMS** (Database Management System) - СУБД, или Система Управления Базами данных. Это весь программный комплекс которые реализует хранение, обработку и обеспечивает доступ к данным. Отдельно выделяются RDBMS где добавляется уточнение что речь идет о реляционных базах данных.

**CRUD (Create Read Update Delete)** - это аналог "hello world" для языков программирования. Базовый набор операций которые должна реализовывать СУБД.


##  Python

Python имеет стандартизированный API - https://www.python.org/dev/peps/pep-0249/

Библиотеки:

- https://docs.python.org/3/library/sqlite3.html
- https://pypi.org/project/mysql-connector-python/
- https://pypi.org/project/psycopg2-binary/

## Основы работы

1) Создать подключение.

```python
import sqlite3

connection = sqlite3.connect("simple.sqlite")
```

```python
import mysql.connector

connection = mysql.connector.connect(user='scott', password='password', host='127.0.0.1', database='employees')
cursor = connection.cursor()
```

```python
import psycopg2

connection = psycopg2.connect(user='db_user', password='mypassword', dbname='database', host='localhost')
cursor = connection.cursor()

```

2) Выполнить необходимые действия (CRUD).

```python
# SQLite
sql = "INSERT INTO {DB_NAME} (name, email, phone, address) VALUES (?, ?, ?, ?)".format(DB=DB_NAME)
data = ("Vasiliy", "vasiliy@mail.ru", "+7999999999", "Moscow")
connection.execute(sql, data)
connection.commit()
```


3) Закрыть подключение.

```python
connection.close()
```


