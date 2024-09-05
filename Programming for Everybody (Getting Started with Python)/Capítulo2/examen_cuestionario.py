x = int(98.6)
print(x)
#comentario
#---------------------
Y = 42
print(Y)
#---------------------
#spam.23 no es nombre de variable
#spam
#X = X + 2

#---------------------
H= 42
W= 10
T = H % W
print(T)
#-----------------------
Q = 1
W = 2
E = 3
R = 8
T = 4
P = Q + W * E - R / T
print(P)
#---------------------
#2.2 Escriba un programa que use input para solicitar a un usuario su nombre y luego les da la bienvenida. Tenga en cuenta que la entrada aparecerá en un cuadro de diálogo. Ingrese Sarah en el cuadro emergente cuando se le solicite que su La salida coincidirá con la salida deseada.
name = input("Enter your name: ")

print(f"Hello {name}")
#2.3 Escribir un programa para solicitar al usuario horas y tarifa por hora usando la entrada para calcular el salario bruto. Utilice 35 horas y una tasa de 2,75 por hora para probar el (el pago debe ser de 96.25). Debe usar la entrada para Lee una cadena y float() para convertir la cadena en un número. No se preocupe por la comprobación de errores o los datos incorrectos del usuario.
# This first line is provided for you

hrs = input("Enter Hours:")
rate = input("Enter Rate: ")

hours = float(hrs)
rate_per_hour = float(rate)


pay = hours * rate_per_hour

print(f"Pay: {pay:.2f}")

