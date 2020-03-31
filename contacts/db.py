import sqlite3

DB = "contacts"


class SqliteConnector:

    def __init__(self, file):
        self.db_file = file
        self.connection = sqlite3.connect(self.db_file)
        with open("sql_templates/contacts.sql", "r") as script:
            self.connection.execute(script.read())
        self.cursor = self.connection

    def __del__(self):
        print('Connection closed!')
        self.connection.close()


def contacts_db():
    return SqliteConnector('simple.sqlite')


def _execute(sql=None, params=None):
    db = contacts_db()
    try:
        if params:
            db.cursor.execute(sql, params)
        else:
            db.cursor.execute(sql)
        db.cursor.commit()
    except sqlite3.OperationalError as e:
        print("Oooops... something is broken")
        print(e)


def insert_contact(params: tuple):
    sql = "INSERT INTO {DB} (name, email, phone, address) VALUES (?, ?, ?, ?)".format(DB=DB)
    _execute(sql=sql, params=params)


def delete_contact(name):
    sql = "DELETE FROM {DB} WHERE name = ?".format(DB=DB)
    _execute(sql=sql, params=(name,))


def select_contact(name):
    db = contacts_db()
    sql = "SELECT * FROM {DB} WHERE name = ?".format(DB=DB)
    result = db.cursor.execute(sql, (name,)).fetchone()
    return result


def get_all_rows():
    # https://stackoverflow.com/questions/31745613/fetching-mysql-data-as-python-dictionary
    db = contacts_db()
    sql = "SELECT * FROM {DB}".format(DB=DB)
    result = db.cursor.execute(sql)
    if result:
        return result.fetchall()
    else:
        return []


def update_contact(name, field, new_value):
    sql = "UPDATE contacts SET {field} = '{new_value}' WHERE name = '{name}'".format(field=field, new_value=new_value,
                                                                                     name=name)
    _execute(sql=sql)
