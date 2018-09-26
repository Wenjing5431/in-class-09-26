import os

from flask import Flask, jsonify, redirect, render_template, request, url_for
import psycopg2

import db

app = Flask(__name__)


@app.before_first_request
def initialize():
    db.setup()


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/people', methods=['GET', 'POST'])
def people():
    if request.method == 'POST':
        # TODO insert the new person into the db
        # request.form['xxxx']
        return redirect(url_for("people"))
    else:
        with db.get_db_cursor() as cur:
            cur.execute("SELECT * FROM person;")
            names = [record["name"] for record in cur]

        return render_template("people.html", names=names)


@app.route('/api/foo')
def api_foo():
    data = {
        "message": "hello, world",
        "isAGoodExample": False,
        "aList": [1, 2, 3],
        "nested": {
            "key": "value"
        }
    }
    # FIXME
    return data


if __name__ == '__main__':
    pass
