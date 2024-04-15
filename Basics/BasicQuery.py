# The code below shows how to get info from a table
# It can be by criteria as show or even a specific field 

import sqlite3

conn = sqlite3.connect('/home/user/SQLite/students.db')
c = conn.cursor()


# Displaying data
c.execute("SELECT * FROM students1 WHERE age=19") 
# Also instead of selecting all, we can put the fields that we want to display(separating their name using commas) 
# This way you can also preset an order for the way that theu will be presented
# Though when doing this remember to remove the [x] next to row so thhat all the data you want to show, shows (unless that's not what you want :) )

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