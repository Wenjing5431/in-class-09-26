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
    link = url_for("people")
    # return f'Hello World! <a href="{link}">people</a>'
    return render_template("home.html", link=link)


@app.route('/people', methods=['GET', 'POST'])
def people():
    if request.method == 'POST':
        name = request.form['name']
        with db.get_db_cursor(commit=True) as cur:
            cur.execute("INSERT INTO person (name) VALUES (%s)", (name,))
        return redirect(url_for("people"))
    else:
        with db.get_db_cursor() as cur:
            cur.execute("SELECT * FROM person;")
            names = [record["name"] for record in cur]

        return render_template("people.html", names=names)

@app.route('/people/<username>', methods=['GET'])
def userprofile(username):
    with db.get_db_cursor() as cur:
        cur.execute("SELECT * FROM person WHERE name = %s;", (username,))
        user = cur.fetchall()
    return render_template("profile.html", user = user[0])

@app.route('/editprofile', methods=['POST'])
def editprofile():
    userid = request.form['userid']
    name = request.form['name']
    with db.get_db_cursor(commit=True) as cur:
        cur.execute("UPDATE person SET name = %s WHERE person_id = %s", (name, userid))
    return redirect(url_for("people"))


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
    return jsonify(data)


if __name__ == '__main__':
    pass
