import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


@app.get('/contacts')
def show_all_contacts():
    conn = get_db_connection()
    contacts = conn.execute('SELECT * FROM contacts').fetchall()
    conn.close()
    print(contacts)
    return render_template('index.html', contacts=contacts)


@app.post('/contact')
def create_contact():
    return "create new contact"
