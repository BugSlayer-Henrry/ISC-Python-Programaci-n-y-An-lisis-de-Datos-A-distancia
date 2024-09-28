import urllib.request, urllib.parse
import json, ssl

# URL del servicio
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    # Preparar los parámetros de la URL
    address = address.strip()
    parms = {'q': address}
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====') 
        print(data)
        break

    # Extraer el plus_code
    if 'plus_code' in js['features'][0]['properties']:
        plus_code = js['features'][0]['properties']['plus_code']
        print('Plus code:', plus_code)
    else:
        print('No plus code found')

    # Extraer latitud y longitud
    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formatted']
    print(location)
