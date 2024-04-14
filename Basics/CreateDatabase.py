import sqlite3

conn = sqlite3.connect('/home/user/SQLite/students.db') #Note that this is an example path on my machine
c = conn.cursor() 

#Creating the table
c.execute('''CREATE TABLE students(
          name TEXT,
          age INTEGER,
          height REAL
    )''')


conn.commit()

c.close()
conn.close()