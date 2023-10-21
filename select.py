# import module sqlite
import sqlite3

# Create Connection or db File
conn = sqlite3.connect('godfather.db')

# select db
cur = conn.cursor()

peoples = cur.execute("SELECT * FROM persons")

for i in peoples:
    print(i[1])

