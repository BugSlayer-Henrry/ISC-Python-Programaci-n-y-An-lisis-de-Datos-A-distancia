import sqlite3

# Conectar a la base de datos (crea el archivo si no existe)
conn = sqlite3.connect('C:/Users/winsl/OneDrive/Escritorio/CONTROLMATECOMPUTACIONAL/Counting_Email_in_a_Database/emaildb.sqlite')
cur = conn.cursor()

# Crear la tabla Counts (la elimina si ya existe)
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)
''')

# Pedir el nombre del archivo
fname = input('Enter file name: ')
if (len(fname) < 1): 
    fname = 'mbox.txt'  # Si no se ingresa un archivo, utiliza 'mbox.txt'

# Abrir el archivo de entrada
try:
    fh = open(fname)
except FileNotFoundError:
    print(f"El archivo {fname} no fue encontrado.")
    exit()

# Procesar cada línea del archivo
for line in fh:
    if not line.startswith('From: '): 
        continue
    pieces = line.split()
    email = pieces[1]  # Extraer el correo
    org = email.split('@')[1]  # Extraer el dominio (organización)

    # Verificar si el dominio ya está en la base de datos
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    
# Guardar (commit) los cambios
conn.commit()

# Realizar una consulta para mostrar los 10 dominios más comunes
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print("\nRecuento de organizaciones:")
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Cerrar la conexión
cur.close()
