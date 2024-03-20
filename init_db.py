"""
@author: Lena

"""

import sqlite3
import csv

# Connect to the SQLite database
connection = sqlite3.connect("database.db")
cur = connection.cursor()

# Create the schema by executing the SQL commands from the schema.sql file
with open("schema.sql") as f:
    connection.executescript(f.read())


# Read data from the Arenas.csv file and insert it into the arenas table
with open("Community_Centres.csv", newline="") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip header row if present
    arenas = [
        (row[0], row[1], row[2], float(row[3]), float(row[4])) for row in csv_reader
    ]
    cur.executemany(
        "INSERT INTO arenas (id, street, company, latitude, longitude) VALUES (?, ?, ?, ?, ?)",
        arenas,
    )

# Read data from the Parks Centroids.csv file and insert it into the parks table
with open("Parks Centroids.csv", newline="") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip header row if present
    park_data = [
        (float(row[0]), float(row[1]), row[2], row[3], row[4]) for row in csv_reader
    ]
    cur.executemany(
        "INSERT INTO parks (latitude, longitude, id, names, street) VALUES (?, ?, ?, ?, ?)",
        park_data,
    )


# Read data from the Community_Centres.csv file and insert it into the centres table
with open("Community_Centres.csv", newline="") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip header row if present
    centres = [
        (row[0], row[1], row[2], float(row[3]), float(row[4])) for row in csv_reader
    ]
    cur.executemany(
        "INSERT INTO centres (id, street, names, latitude, longitude) VALUES (?, ?, ?, ?, ?)",
        centres,
    )


# Read data from the Fires_Stations.csv file and insert it into the fire table
with open("Fire_Stations.csv", newline="") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip header row if present
    fire = [
        (row[0], row[1], row[2], float(row[3]), float(row[4])) for row in csv_reader
    ]
    cur.executemany(
        "INSERT INTO fire (id, street, names, latitude, longitude) VALUES (?, ?, ?, ?, ?)",
        fire,
    )

# Read data from the Libraries.csv file and insert it into the libraries table
with open("Libraries.csv", newline="") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip header row if present
    libraries = [
        (float(row[0]), float(row[1]), row[2], row[3], row[4], row[5])
        for row in csv_reader
    ]
    cur.executemany(
        "INSERT INTO libraries (latitude, longitude, id, names, street, link) VALUES (?, ?, ?, ?, ?, ?)",
        libraries,
    )


# Read data from the Hospitals.csv file and insert it into the hospitals table
with open("Hospitals.csv", newline="") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip header row if present
    hospitals = [
        (float(row[0]), float(row[1]), row[2], row[3], row[4], row[5])
        for row in csv_reader
    ]
    cur.executemany(
        "INSERT INTO hospitals (latitude, longitude, id, names, street, facility) VALUES (?, ?, ?, ?, ?, ?)",
        hospitals,
    )


# Commit the transaction and close the connection
connection.commit()
connection.close()
