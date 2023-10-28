import sqlite3

conn = sqlite3.connect('dr.db')
cur = conn.cursor()


cur.execute("DELETE FROM people WHERE name='ali'")

conn.commit()