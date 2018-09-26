import os

from flask import Flask, render_template, url_for
import psycopg2

import db

app = Flask(__name__)

@app.before_first_request
def initialize():
    db.setup()

@app.route('/')
def hello_world():
    link = url_for("people")
    return f'Hello World! <a href="{link}">people</a>'

@app.route('/people')
def people():
    with db.get_db_cursor() as cur:
        cur.execute("SELECT * FROM person;")
        names = [record["name"] for record in cur]

    return render_template("people.html", names=names)

if __name__ == '__main__':
    pass
