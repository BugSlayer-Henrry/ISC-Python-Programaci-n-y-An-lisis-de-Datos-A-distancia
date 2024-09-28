import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('C:\\Users\\winsl\\OneDrive\\Escritorio\\ISC-Python-Programaci-n-y-An-lisis-de-Datos-A-distancia\\Capstone Retrieving, Processing, and Visualizing Data with Python\\spider.sqlite')
cur = conn.cursor()

print("Clasificación de páginas (Top 10):")

cur.execute('''SELECT id, url, new_rank FROM Pages ORDER BY new_rank DESC LIMIT 10''')
for row in cur.fetchall():
    print(row)

conn.close()
