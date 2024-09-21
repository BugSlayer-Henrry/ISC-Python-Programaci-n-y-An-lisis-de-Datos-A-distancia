#CONTRAR NÚMEROS Y SUMAR EL TOTAL DE NÚMEROS ENCONTRADOS EN UN TEXTO

import re

# Especifica la ruta completa al archivo
with open(r'C:\Users\winsl\OneDrive\Escritorio\ISC-Python-Programaci-n-y-An-lisis-de-Datos-A-distancia\Using Python to Access Web Data\regex_sum_2075385.txt') as file:
    contents = file.read()

numbers = re.findall('[0-9]+', contents)

# Imprimir los números encontrados
print("Números encontrados:", numbers)

total_sum = sum(int(num) for num in numbers)

print("Suma:", total_sum)
