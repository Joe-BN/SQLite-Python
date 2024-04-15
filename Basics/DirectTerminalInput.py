# This is just an example of how to make your life easier when inputing data to the table
# As is the loop is not entirely safe since my variables are not checked, hence there can be errors like using numbers as names
# Feel free to mod this file for your use


import sqlite3

conn = sqlite3.connect('/home/phate/Env/Dev-01/Code/SQLite02/students1.db')
c = conn.cursor()


#Inserting data
number = 1

while number <2:
    name = input(f"Input name for entry {number}: ")
    age = input(f"input age for {name}: ")
    height= input("Suggest a height for new User: ")
    c.execute('''
        INSERT INTO students1 (number, name, age, height) VALUES (?, ?, ?, ?)
        ''',
        (number, name, age, height))
    conn.commit()
    number += 1

# Displaying data
c.execute("SELECT * FROM students1")
for name in c.fetchall:
    print(name)

conn.commit()

c.close()
conn.close()

#The input method I've used above may seem pointless but is usefull as a way to put in multiple prediterminrd value: using the tuple


#A better way to go round this is to use the following:

#while number < x:
#    name = input(f"Input name for entry {number}: ")
#    age = input(f"input age for {name}: ")
#    height= input("Suggest a height for new User: ")

#    c.execute('''
#        INSERT INTO students1 (number, name, age, height) VALUES (?, ?, ?, ?)
#        ''',
#        (number, name, age, height))
#    conn.commit()
#    number += 1


#An issue to note with this code is that every time it runs, counter starts from Zero
