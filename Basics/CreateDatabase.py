import sqlite3

conn = sqlite3.connect('/home/phate/Env/Dev-01/Code/SQLite02/students.db')
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