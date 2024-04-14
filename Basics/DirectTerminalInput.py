# This is just an example of how to make your life easier when inputing data to the table
# As is the loop is not entirely safe since my variables are not checked, hence there can be errors like using numbers as names
# Feel free to mod this file for your use


import sqlite3

conn = sqlite3.connect('/home/user/SQLite/students1.db')
c = conn.cursor()

# Inserting data
number = 1

while number <=5:
    name = input(f"Input name for entry {number}: ")
    age = input(f"input age for {name}: ")
    height= input("Suggest a height for new User: ")
    User_details_list = [
        (number, name, age, height)
    ]
    c.executemany('''
        INSERT INTO students1 (number, name, age, height) VALUES (?, ?, ?, ?)
        ''',
        User_details_list)
    conn.commit()
    number += 1

# Displaying data
names = c.execute("SELECT * FROM students1")
for name in names:
    print(c.fetchall())

conn.commit()

c.close()
conn.close()