# This table shows how to delete records in tables
 
import sqlite3

conn = sqlite3.connect('/home/user/SQLite/students.db')
c = conn.cursor()

value = 1.5

# This is just an example of correcting a mistake I made when testing the database
c.execute('''
              DELETE FROM students1
              WHERE name = 1.5;            
    ''')

# Displaying data
names = c.execute("SELECT * FROM students1")
for name in names:
    print(c.fetchall())

conn.commit()

c.close()
conn.close()