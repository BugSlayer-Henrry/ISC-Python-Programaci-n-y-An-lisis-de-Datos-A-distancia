import sqlite3 
import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup
import re
import os
import json  # Importar el módulo JSON

# Ruta del archivo de la base de datos
db_path = r'C:\Users\winsl\OneDrive\Escritorio\ISC-Python-Programaci-n-y-An-lisis-de-Datos-A-distancia\Capstone Retrieving, Processing, and Visualizing Data with Python\spider.sqlite'

# Verificar si el archivo existe y eliminarlo (después de cerrar la conexión)
if os.path.exists(db_path):
    print("El archivo está siendo eliminado...")
    try:
        os.remove(db_path)
        print(f"Archivo {db_path} eliminado.")
    except PermissionError as e:
        print(f"No se pudo eliminar el archivo: {e}")
else:
    print("El archivo no existe.")

# Crear o conectar a la base de datos (después de intentar eliminar el archivo)
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Crear tabla si no existe
cur.execute('''CREATE TABLE IF NOT EXISTS Pages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT UNIQUE,
    retrieved INTEGER
)''')

# Ignorar errores de certificados SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def store_url(url):
    """
    Inserta la URL en la base de datos si no existe ya.
    """
    cur.execute('INSERT OR IGNORE INTO Pages (url, retrieved) VALUES (?, 0)', (url,))
    conn.commit()  # Guardar cambios en la base de datos

def get_links(url):
    """
    Obtiene los enlaces de la página dada y los almacena en la base de datos.
    """
    # Verificar si ya se ha recuperado esta URL
    cur.execute('SELECT retrieved FROM Pages WHERE url = ? LIMIT 1', (url,))
    row = cur.fetchone()
    if row is not None and row[0] == 1:
        print(f"La URL {url} ya ha sido recuperada.")
        return []

    try:
        # Intentar recuperar la página
        response = urllib.request.urlopen(url, context=ctx)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e.code} al recuperar {url}")
        return []
    except urllib.error.URLError as e:
        print(f"URLError: {e.reason} al recuperar {url}")
        return []
    except Exception as e:
        print(f"Error desconocido al recuperar {url}: {e}")
        return []

    # Almacenar URL en la base de datos como "recuperada"
    store_url(url)
    cur.execute('UPDATE Pages SET retrieved = 1 WHERE url = ?', (url,))
    conn.commit()

    links = []
    tags = soup('a')
    for tag in tags:
        href = tag.get('href', None)
        if href is None:
            continue
        # Convertir URL relativa en absoluta
        full_url = urllib.parse.urljoin(url, href)

        # Ignorar enlaces que no son válidos (e.g., mailto: o javascript:)
        if not re.match(r'^https?://', full_url):
            continue
        
        links.append(full_url)
    
    return links

def valid_link(link):
    """
    Filtra enlaces que ya se hayan procesado o no sean válidos.
    """
    cur.execute('SELECT id FROM Pages WHERE url = ? LIMIT 1', (link,))
    row = cur.fetchone()
    return row is None

def generate_json(db_path):
    """
    Genera un archivo JSON con las URLs y su estado de recuperación en la misma ruta que spider.sqlite.
    """
    cur.execute('SELECT url, retrieved FROM Pages')
    rows = cur.fetchall()
    
    data = []
    for url, retrieved in rows:
        data.append({
            'url': url,
            'retrieved': bool(retrieved)  # Convertir a booleano
        })

    # Generar la ruta para el archivo JSON en la misma carpeta que spider.sqlite
    json_path = os.path.join(os.path.dirname(db_path), 'spider.json')

    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump({'pages': data}, json_file, ensure_ascii=False, indent=4)
    print(f"Archivo JSON generado con éxito: {json_path}")

# Iniciar el proceso de crawling
start_url = input("Enter URL: ")  # Pedir la URL de inicio
if len(start_url) < 1:
    start_url = 'http://python-data.dr-chuck.net/'  # URL por defecto

valid_links_list = [start_url]

# Continuar buscando hasta que la base de datos tenga al menos 100 registros
while True:
    # Verificar cuántas URL ya se han almacenado en la base de datos
    cur.execute('SELECT COUNT(*) FROM Pages')
    count = cur.fetchone()[0]
    
    if count >= 100:
        print("Se alcanzó el límite de 100 URL almacenadas.")
        break

    if len(valid_links_list) == 0:
        print("No quedan más enlaces para procesar.")
        break

    next_url = valid_links_list.pop(0)
    print(f"Crawling: {next_url}")

    # Obtener enlaces desde la URL actual y filtrar enlaces válidos
    new_links = get_links(next_url)
    new_links = [link for link in new_links if valid_link(link)]
    valid_links_list.extend(new_links)

# Generar el archivo JSON después de completar el crawling
generate_json(db_path)

# Cerrar la conexión a la base de datos
cur.close()
conn.close()
