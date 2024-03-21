
DROP TABLE IF EXISTS arenas;

CREATE TABLE arenas (
    id INTEGER PRIMARY KEY,
    company TEXT NOT NULL,
    street TEXT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL
);


DROP TABLE IF EXISTS parks;

CREATE TABLE parks (
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    id INTEGER PRIMARY KEY,
    names TEXT NOT NULL,
    street TEXT NOT NULL
);

DROP TABLE IF EXISTS centres;

CREATE TABLE centres (
    id INTEGER PRIMARY KEY,
    street TEXT NOT NULL,
    names TEXT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL
);

DROP TABLE IF EXISTS fire;

CREATE TABLE fire (
    id INTEGER PRIMARY KEY,
    street TEXT NOT NULL,
    names TEXT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL
);

DROP TABLE IF EXISTS libraries;

CREATE TABLE libraries (
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    id INTEGER PRIMARY KEY,
    names TEXT NOT NULL,
    street TEXT NOT NULL,
    link TEXT NOT NULL
);

DROP TABLE IF EXISTS hospitals;

CREATE TABLE hospitals (
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    id INTEGER PRIMARY KEY,
    names TEXT NOT NULL,
    street TEXT NOT NULL,
    facility TEXT NOT NULL
);
