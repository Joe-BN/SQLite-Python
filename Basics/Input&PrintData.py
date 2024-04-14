import sqlite3

conn = sqlite3.connect('/home/user/SQLite/students.db') # Just a sample path from my machine 
c = conn.cursor()

# Inserting data
c.execute("INSERT INTO students VALUES ('mark', 20, 1.9)")

# Displaying data
c.execute("SELECT * FROM students")
print(c.fetchall())

conn.commit()

c.close()
conn.close()