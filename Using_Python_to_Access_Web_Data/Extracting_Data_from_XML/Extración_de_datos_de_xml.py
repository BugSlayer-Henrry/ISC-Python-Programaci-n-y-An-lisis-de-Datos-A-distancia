import urllib.request
import xml.etree.ElementTree as ET

# Bienvenido Henrry Bolaños Rodriguez de Using Python to Access Web Data
print("Bienvenido Henrry Bolaños Rodriguez de Using Python to Access Web Data")

# Solicitar la URL
url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)

# Leer los datos XML desde la URL
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

# Analizar los datos XML
tree = ET.fromstring(data)

# Encontrar todos los elementos 'count'
counts = tree.findall('.//count')
nums = list()

# Extraer los valores y convertirlos a enteros
for result in counts:
    nums.append(int(result.text))  # Convertir el texto a entero y agregarlo a la lista nums

print('Count:', len(nums))
print('Sum:', sum(nums))