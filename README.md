# sqlite_python
working with sqlite in pythonDeleting, editing, displaying single and displaying all information from the database.
Using standard Python modules.
`its just practice for students`

<hr>

# Document

## Structure

for work and connect to db we need import `sqlite` module:
```python
import sqlite
```

> we do not need to install this module

## duty

### for make new connection:
```python
conn = sqlite3.connect("your-db-name.db")
```

if the db was found connect to that and if db not found create that.

### create query

1. befure create query we need to select the db:
```python
cur = conn.curser()
```
2. now with this code we can make query to db:
```python
    cur.execute("CREATE TABLE persons(name varchar(100),number,age int)")
```
3. now we must save all changes on db:
```python
conn.commit()
```
