from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Recuperar todas las etiquetas <span>
tags = soup('span')
sum_numbers = 0
count = 0

for tag in tags:
    # Extraer el contenido de texto y convertirlo a entero
    number = int(tag.contents[0])
    sum_numbers += number
    count += 1

print('Count', count)
print('Sum', sum_numbers)
