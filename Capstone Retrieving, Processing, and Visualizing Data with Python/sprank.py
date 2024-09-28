import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('C:\\Users\\winsl\\OneDrive\\Escritorio\\ISC-Python-Programaci-n-y-An-lisis-de-Datos-A-distancia\\Capstone Retrieving, Processing, and Visualizing Data with Python\\spider.sqlite')
cur = conn.cursor()

# Verificar si la columna new_rank existe, si no, agregarla
try:
    cur.execute('ALTER TABLE Pages ADD COLUMN new_rank INTEGER')
    print("Columna 'new_rank' agregada a la tabla 'Pages'.")
except sqlite3.OperationalError:
    # La columna ya existe, podemos continuar
    print("La columna 'new_rank' ya existe. Continuando...")

# Actualizar el nuevo ranking
cur.execute('UPDATE Pages SET new_rank = RANDOM() % 100')  # Simulando un ranking aleatorio
print("Ranking actualizado para las páginas.")

# Guardar cambios
conn.commit()
print("Cambios guardados.")

# Cerrar conexión
conn.close()
print("Conexión cerrada.")
