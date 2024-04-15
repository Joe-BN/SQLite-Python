# The code below shows how to get info from a table
# It can be by criteria as show or even a specific field 

import sqlite3

conn = sqlite3.connect('/home/user/SQLite/students.db')
c = conn.cursor()


# Displaying data
c.execute("SELECT * FROM students1 WHERE age=19") 
#The = sumbol can be replaces by logic operators eg: > incluting and 'and' for specified ranges
total = 0
for row in c.fetchall():
    print(row)
    total+= 1

    # Below only refernces a specific field
    print(row[0])

print (total)

conn.commit()

c.close()
conn.close()