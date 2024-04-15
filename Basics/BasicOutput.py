# This program outputs each record in the table mentioned
# Its also counts the number of records and displays it

import sqlite3

conn = sqlite3.connect('/home/user/SQLite/students.db')
c = conn.cursor()

# Displaying data
names = c.execute("SELECT * FROM students1")
total = 0
for name in names:
    print(c.fetchone())
    total+= 1

print (total)

conn.commit()

c.close()
conn.close()