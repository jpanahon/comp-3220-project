import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__)

# run: cd comp-3220-project-main, export flask_app=testapp.py, flask run


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# open index template
@app.route("/")
def index():
    return render_template("index.html") 


@app.route("/arenas")
def arenas():
    conn = get_db_connection()
    arenas = conn.execute("SELECT * FROM arenas").fetchall()
    conn.close()
    return render_template("arenas.html", arenas=arenas)


@app.route("/parks")
def parks():
    conn = get_db_connection()
    parks = conn.execute("SELECT * FROM parks").fetchall()
    conn.close()
    return render_template("parks.html", parks=parks)


@app.route("/centres")
def centres():
    conn = get_db_connection()
    centres = conn.execute("SELECT * FROM centres").fetchall()
    conn.close()
    return render_template("centres.html", centres=centres)


@app.route("/fire")
def fire():
    conn = get_db_connection()
    fire = conn.execute("SELECT * FROM fire").fetchall()
    conn.close()
    return render_template("fire.html", fire=fire)


@app.route("/libraries")
def libraries():
    conn = get_db_connection()
    libraries = conn.execute("SELECT * FROM libraries").fetchall()
    conn.close()
    return render_template("libraries.html", libraries=libraries)


@app.route("/hospitals")
def hospitals():
    conn = get_db_connection()
    hospitals = conn.execute("SELECT * FROM hospitals").fetchall()
    conn.close()
    return render_template("hospitals.html", hospitals=hospitals)
