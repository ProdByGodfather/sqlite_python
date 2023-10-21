# import module sqlite
import sqlite3

# Create Connection or db File
conn = sqlite3.connect('godfather.db')

# select db
cur = conn.cursor()

try:
    # ساختن جدول انسان ها با یک ای دی یک نام یک شماره و یک سن
    cur.execute("CREATE TABLE persons(name varchar(100),number,age int)")
except:
    pass

# ذخیره کردن کد های sql
conn.commit()

name = input("Enter Name: ")
number = input("Enter Number: ")
age = int(input("Enter Age: "))

# QUERY پرس و جو
lists = [name,number,age]
cur.execute("INSERT INTO persons VALUES(?,?,?)",lists)
# ذخیره کردن کد های sql
conn.commit()