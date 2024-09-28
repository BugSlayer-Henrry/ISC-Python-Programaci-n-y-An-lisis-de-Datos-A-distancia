import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Entrada del usuario
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Ciclo para seguir enlaces
for i in range(count):
    print(f'Retrieving: {url}')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Recuperar todos los enlaces
    tags = soup('a')
    if position <= len(tags):
        url = tags[position - 1].get('href', None)
    else:
        print("Position is out of range.")
        break

# Imprimir el apellido recuperado
print(f'La respuesta a la tarea es: {tags[position - 1].get_text()}')
