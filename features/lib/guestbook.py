import sqlite3 as sql
from datetime import datetime

con = sql.connect('guestbook.db')
db = con.cursor()

class GuestBook(object):
    def init_db(self):
        db.execute('''CREATE TABLE guestbook (name varchar, date date)''')
        con.commit()

    def add(self, guest):
        today = datetime.today()
        entry = (guest, today,)
        db.execute('INSERT INTO guestbook VALUES (?, ?)', entry)
        con.commit()
        return db.fetchone()

    def list(self):
        db.execute('SELECT * FROM guestbook')
        return db.fetchall()
        # print(db.fetchall())

    def reset_db(self):
        db.execute('DELETE FROM guestbook')
        con.commit()
        return "Guestbook table has been reset."

    def close_db(self):
        con.close()


  