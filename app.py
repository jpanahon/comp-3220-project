import sqlite3
from flask import Flask, jsonify, render_template, request 


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


@app.route("/map")
def map():
    return render_template("map.html")

@app.route('/get_location')
def get_location():
    location_type = request.args.get('type')
    location_id = request.args.get('id')
    jsonify()

    conn = get_db_connection()
    cursor = conn.cursor()

    location_type_index = {"library": "libraries", "park": "parks", 
                           "bus": "bus", "fire": "fire", "centre": "centres", 
                           "arena": "arenas", "hospital": "hospitals"}
    # if location_type == 'library':
    #     cursor.execute("SELECT street FROM libraries WHERE id=?", (location_id,))
    # elif location_type == 'park':
    #     cursor.execute("SELECT street FROM parks WHERE id=?", (location_id,))
    # elif location_type == 'bus':
    #     cursor.execute("SELECT street FROM bus WHERE id=?", (location_id,))
    # elif location_type == 'fire':
    #     cursor.execute("SELECT street FROM fire WHERE id=?", (location_id,))
    # elif location_type == 'centre':
    #     cursor.execute("SELECT street FROM centres WHERE id=?", (location_id,))
    # elif location_type == 'arena':
    #     cursor.execute("SELECT street FROM arenas WHERE id=?", (location_id,))
    # elif location_type == 'hospital':
    #     cursor.execute("SELECT street FROM hospitals WHERE id=?", (location_id,))
    # else:
    #     return jsonify({'error': 'Invalid location type'}), 400 

    try:
        cursor.execute("SELECT street FROM ? WHERE id=?", (location_type_index[location_type], location_id,))
    except Exception:
        return jsonify({'error': 'Invalid location type'}), 400 

    result = cursor.fetchone()
    conn.close()

    if result:
        return jsonify({'address': result['street']})  
    else:
        return jsonify({'error': 'Location not found'}), 404  
