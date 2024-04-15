# This program outputs each record in the table mentioned
# Its also counts the number of records and displays it

import sqlite3

conn = sqlite3.connect('/home/phate/Env/Dev-01/Code/SQLite02/students1.db')
c = conn.cursor()

# Displaying data
c.execute("SELECT * FROM students1")
total = 0
for row in c.fetchall():
    print(row)
    total+= 1

print (total)

conn.commit()

c.close()
conn.close()