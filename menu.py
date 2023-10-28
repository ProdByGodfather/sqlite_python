import tkinter as tk
import sqlite3

conn = sqlite3.connect('dr.db')
cur = conn.cursor()

M = cur.execute("SELECT * FROM people")



win = tk.Tk()
win.title("Godfather")

menu = tk.Menu(win)
win.config(menu=menu)
filemenu = tk.Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New contact') 
# کشیدن خط
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=win.quit) 
helpmenu = tk.Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 


lb = tk.Listbox(win)

j = 1
for i in M:
    lb.insert(j,f"Name: {i[0]}\t Age:{i[1]}")
    j+=1

lb.pack()



win.mainloop()