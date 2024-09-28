import sqlite3
import csv
import os

# Ruta al archivo CSV
csv_file_path = r'C:\Users\winsl\OneDrive\Escritorio\CONTROLMATECOMPUTACIONAL\python2\tracks.csv'

# Ruta para la base de datos SQLite
db_file_path = r'C:\Users\winsl\OneDrive\Escritorio\CONTROLMATECOMPUTACIONAL\python2\trackdb.sqlite'

# Conectar a la base de datos
conn = sqlite3.connect(db_file_path)
cur = conn.cursor()

# Crear las tablas
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Abrir el archivo CSV
with open(csv_file_path, 'r', encoding='utf-8') as handle:
    reader = csv.reader(handle)
    # Saltar la primera línea si tiene encabezados
    next(reader)

    for pieces in reader:
        if len(pieces) < 6:
            continue

        name = pieces[0]
        artist = pieces[1]
        album = pieces[2]
        genre = pieces[3]  # Asumir que el género está en la columna 4
        count = pieces[4]
        rating = pieces[5]
        length = pieces[6]

        # Insertar o ignorar el artista
        cur.execute('''INSERT OR IGNORE INTO Artist (name) 
            VALUES ( ? )''', (artist, ))
        cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
        artist_id = cur.fetchone()[0]

        # Insertar o ignorar el álbum
        cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
            VALUES ( ?, ? )''', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
        album_id = cur.fetchone()[0]

        # Insertar o ignorar el género
        cur.execute('''INSERT OR IGNORE INTO Genre (name) 
            VALUES ( ? )''', (genre, ))
        cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
        genre_id = cur.fetchone()[0]

        # Insertar la pista
        cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, genre_id, len, rating, count) 
            VALUES ( ?, ?, ?, ?, ?, ? )''', 
            (name, album_id, genre_id, length, rating, count))

    conn.commit()

# Cerrar la conexión
conn.close()
