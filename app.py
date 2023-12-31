import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

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
    return render_template('index.html', contacts=contacts)


@app.get('/contact')
def get_contact():
    id_user = request.args.get('id')

    conn = get_db_connection()
    query = 'SELECT * FROM contacts where id = {}'.format(id_user)
    print(query)
    contact = conn.executescript(query).fetchone()
    conn.close
    return render_template('contact_page.html', contact=contact)


@app.post('/contact')
def create_contact():
    name = request.form['name']
    last_name = request.form['last_name']

    if not name:
        flash('Name is required!')
    elif not last_name:
        flash('Last Name is required!')
    else:
        conn = get_db_connection()
        conn.execute('INSERT INTO contacts (name, last_name) VALUES (?, ?)',
                     (name, last_name))
        conn.commit()
        conn.close()
        return redirect(url_for('show_all_contacts'))


@app.get('/newcontact')
def new_contact():
    return render_template('create.html')
