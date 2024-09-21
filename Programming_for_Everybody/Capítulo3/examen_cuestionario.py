


# Definir el valor de las variables
_XYScrollCommand = 5  # Asigna un valor a _XYScrollCommand
x = 6  # Asigna un valor a x

# Primer bloque if
if _XYScrollCommand == 5:
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
    #---------------------

    # Segundo bloque if (dentro del primero)
    if x == 6:
        print('Is 6')
        print('Is Still 6')
        print('Third 6')
        print('')
#--------------------------
x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')
#------------------------
if x < 2 :
    print('Below 2')
elif x >= 2 :
     print('Two or more')
else :
    print('Something else')
    #---------------------------

astr = 'Hello Bob'  # No se puede convertir a entero, se mantiene en la variable
try:
    istr = int(astr)  # Esto fallará
except ValueError:
    print('Error: No se puede convertir a entero', astr)
    istr = None  # Puedes definir un valor por defecto o manejar el error de otra manera

print('First', istr)  # Esto imprimirá 'First None' o 'Error: No se puede convertir a entero Hello Bob'

astr = '123'  # Esto es una cadena válida para conversión
istr = int(astr)  # Esto funcionará correctamente
print('Second', istr)  # Esto imprimirá 'Second 123'
print('')
#------------------------
astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1

#---------------------
# Solicitar al usuario la cantidad de horas trabajadas
hrs = input("Enter Hours: ")
h = float(hrs)

# Solicitar al usuario la tarifa por hora
rate = input("Enter Rate: ")
ra = float(rate)

# Calcular el salario bruto
if h > 40:
    # Pago para las primeras 40 horas
    pay_regular = 40 * ra
    # Pago para las horas extras
    pay_for_hrs_extra = (h - 40) * (ra * 1.5)
    # Salario bruto total
    pay_bruto = pay_regular + pay_for_hrs_extra
else:
    # Solo horas regulares
    pay_bruto = h * ra

# Imprimir el salario bruto
print("Pay:", pay_bruto)

print('')
print('')

######################
score = input("Enter Score: ")

try:
    score = float(score)
except ValueError:
    print("Error: Entrada no válida. Debe ser un número dentro del rango .")
    exit()

# Verificar si la puntuación está en el rango permitido
if 0.0 <= score <= 1.0:
    # Determinar la calificación basada en la puntuación
    if score >= 0.9:
        grade = 'A'
        
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    
    # Imprimir la calificación
    print(grade)
else:
    # Imprimir un mensaje de error si la puntuación está fuera del rango
    print("Error: La puntuación no esta dentro del rango 0.0 a 1.0")

#------------------









