#!/usr/bin/env python
# encoding: utf-8

import os
import sqlite3
from flask import Flask, request, session, g
from flask import redirect, url_for, abort
from flask import render_template, flash


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'data.sqlite3'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='admin',
))
app.config.from_envvar('FLASH_SETTINGS', silent=True)


def connect_db():
    """
    connnects to the specific database.
    """
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """
    open a new database connect if necesarry.
    """
    if not hasattr(g, 'sqlite3_db'):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db


@app.teardown_appcontext
def close_db(error):
    """
    close the database again at the end of the request
    """
    if hasattr(g, 'sqlite3_db'):
        g.sqlite3_db.close()


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('data.sqlite3', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/')
def show_entries():
    db = get_db()
    cursor = db.execute('select title, text from entries order by id desc')
    entries = cursor.fetchall()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entries():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
               [request.form['title'], request.form['text']])

    db.commit()
    flash('new entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Involid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == "__main__":
    app.run()
