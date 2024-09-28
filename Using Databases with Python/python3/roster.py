import time
import json
import sqlite3
import sys

# Parte 1: Crear la base de datos
dbname = r"C:\Users\winsl\OneDrive\Escritorio\CONTROLMATECOMPUTACIONAL\python3\roster_data.sqlite"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# Establecer un temporizador de 2 minutos (120 segundos)
start_time = time.time()

cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    );

    CREATE TABLE Member (
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY(user_id, course_id)
    )
''')

# Parte 2: Deserializar los datos
filename = r"C:\Users\winsl\OneDrive\Escritorio\CONTROLMATECOMPUTACIONAL\python3\roster_data.json"
with open(filename) as jsondata:
    data = json.load(jsondata)

# Parte 3: Insertar datos
for entry in data:
    if time.time() - start_time > 4:  # Verificar si han pasado 2 minutos
        print("El tiempo límite de 2 minutos ha sido alcanzado. Terminando el programa...")
        cur.close()
        conn.close()
        sys.exit()  # Terminar el programa después de 2 minutos

    user = entry[0]
    course = entry[1]
    instructor = entry[2]

    # Insertar usuario
    user_statement = """INSERT OR IGNORE INTO User(name) VALUES(?)"""
    cur.execute(user_statement, (user,))

    # Insertar curso
    course_statement = """INSERT OR IGNORE INTO Course(title) VALUES(?)"""
    cur.execute(course_statement, (course,))

    # Obtener ID del curso
    cur.execute("""SELECT id FROM Course WHERE title = ?""", (course,))
    course_row = cur.fetchone()
    if course_row is None:
        continue  # Salir si no se encuentra el curso
    courseID = course_row[0]

    # Obtener ID del usuario
    cur.execute("""SELECT id FROM User WHERE name = ?""", (user,))
    user_row = cur.fetchone()
    if user_row is None:
        continue  # Salir si no se encuentra el usuario
    userID = user_row[0]

    # Insertar la entrada
    member_statement = """INSERT INTO Member(user_id, course_id, role)
        VALUES(?, ?, ?)"""
    cur.execute(member_statement, (userID, courseID, instructor))

# Guardar los cambios
conn.commit()

# Parte 4: Probar y obtener resultados
# Consulta que concatena 'XYZZY' al valor hexadecimal generado
test_statement = """
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1
"""
cur.execute(test_statement)
result = cur.fetchone()
if result:
    print("RESULT: " + str(result[0]))  # Asegurarse de imprimir el primer elemento

# Cerrar la conexión
cur.close()
conn.close()
