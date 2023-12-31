import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO contacts (name, last_name) VALUES (?, ?)",
            ('Gabriel', 'Aquino')
            )

cur.execute("INSERT INTO contacts (name, last_name) VALUES (?, ?)",
            ('Pedro', 'Horchulhack')
            )

connection.commit()
connection.close()
