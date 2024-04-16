import sqlite3

conn = sqlite3.connect('/home/phate/Env/Dev-01/Code/SQLite02/students1.db')
c = conn.cursor()


height = 0.009
ages = 15

c.execute('''
          UPDATE students1 SET height=(?) WHERE age>(?)
          ''',
          (height, ages))

check = 18
c.execute("SELECT * FROM students1 WHERE age>(?)", (check,))
# Note the ',' after check:
# This is because the program only accepts tuples as iterable arguments
# So adding the comma makes it tuple of length one with iten check only

# If you don't add the comma you'll get an error;
#   .execute("SELECT * FROM students1 WHERE age>(?)", (check))
# sqlite3.ProgrammingError: parameters are of unsupported type

[print(row) for row in c.fetchall()]


conn.commit()

c.close()
conn.close()