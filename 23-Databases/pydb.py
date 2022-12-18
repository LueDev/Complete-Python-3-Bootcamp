import sqlite3

'''
We can either pass the name of a database or write ':memory:' to keep the db in RAM, instead of Disk. 
    This would be ideal for temporary information 
'''

conn = sqlite3.connect(":memory:") 

#Allows us to work with the database 
c = conn.cursor()

'''
If instead we pass a string to connet() as the name of a database, a db will appear in our explorer.
NOTE: Be mindful where the cwd is pointing to (most likely parent) and specify the child actual dir we're working in before creating the db.
'''
conn2 = sqlite3.connect("Sample.db") 
d = conn2.cursor()


#Allows us to run SQL directly to the db. 
c.execute('CREATE TABLE book(title TEXT, pages INTEGER)')

#Since execute() is expecting a string, use the three quotation marks to format the string closer to how it's seen in SQL 
d.execute('''CREATE TABLE IF NOT EXISTS book
             (title TEXT, pages INTEGER)''')


books = [
    ('Are you my mother?', 72),
    ('The Giver', 500),
    ('Once upon a November',63)
]

#Executemany() allows a func to be passed to param1 and a sequence of iterable arguments as Param2
d.executemany('INSERT INTO book VALUES(?, ?)',books)

#The commit func is used to insert data into the table. It uses the connection object rather than the cursor.
conn2.commit()

#SELECT statement retrieves data from the db within conditions. 
d.execute('SELECT * FROM book')

#fetchall() grabs the full list of rows found in the db 
data = d.fetchall()
print(data)

d.execute('DELETE FROM book WHERE title="Are you my mother?"')
conn2.commit()

d.execute('SELECT rowid, title FROM book')
data = d.fetchall()
print(data)

'''Currently stopped at 5:18:18  -- Going to bed
https://www.codebreakthrough.com/view/courses/ultimate-programming-all-in-one-tutorials/507617-python/1469405-python-programming-all-in-one-tutorial-series'''