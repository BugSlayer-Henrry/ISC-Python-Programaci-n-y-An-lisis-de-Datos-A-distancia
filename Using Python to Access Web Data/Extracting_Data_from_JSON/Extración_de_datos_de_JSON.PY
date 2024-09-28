import urllib.request
import json

# URL de tus datos
url = 'http://py4e-data.dr-chuck.net/comments_2075390.json'

# Recuperar y leer los datos
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

# Cargar los datos JSON
info = json.loads(data)

# Sumar los conteos de comentarios
total_sum = sum(comment['count'] for comment in info['comments'])
print('Count:', len(info['comments']))
print('Sum:', total_sum)
