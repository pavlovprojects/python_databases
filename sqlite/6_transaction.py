import sqlite3

con = sqlite3.connect("db.sqlite")

DB = 'contacts'

sql_1 = "INSERT INTO {DB} (name, email) VALUES (?, ?)".format(DB=DB)
sql_2 = "UPDATE {DB} SET nickname = ? WHERE email = ?".format(DB=DB)
sql_3 = "DELETE FROM {DB} WHERE nickname = ?".format(DB=DB)

name = 'SuperUser'
new_name = 'NEW_USER'
email = 'superemail@email.ru'
address = 'California'

con.execute(sql_1, (name, email))
con.execute(sql_2, (new_name, email))
con.commit()
con.rollback()
con.execute(sql_3, (name,))
con.rollback()
con.commit()

con.close()
