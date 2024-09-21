#n = 5
#while n > 0 :
#    print(n)
#print('All done')
#---------
#tot = 0
#for i in [5, 4, 3, 2, 1] :
#    tot = tot + 1
#print(tot)
#----------------
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
     print('Happy New Year:',  friend)
print('Done!')
#-----------------
zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)
#--------------------
smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)
#------------------
# Definir las variables
smallest = None
value = 10

# Aplicar la condición
if smallest is None:
    smallest = value

# Imprimir el resultado
print("Smallest:", smallest)

#----------------------
n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')

#-----------------
#5.2 Write a program that repeatedly 
# prompts a user for integer numbers 
# until the user enters 'done'. Once 
# 'done' is entered, print out the
#  largest and smallest of the numbers.
#  If the user enters anything other than
#  a valid number catch it with a try/except
#  and put out an appropriate message and ignore
#  the number. Enter 7, 2, bob, 10, and 4 and 
# match the output below
largest = None
#smallest = None

#while True:
#    num = input("Enter a number: ")
#
 #   if num == "done":
  #      break

   # try:
    #    numero = int(num)
    #except ValueError:
     #   print("Invalid input")
      #  continue
#
 #   if largest is None or numero > largest:
  #      largest = numero
   # if smallest is None or numero < smallest:
    #    smallest = numero

print("Maximum is", largest)
print("Minimum is", smallest)

#---------------------

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)


#-------------

print(len('banana')*7)
#-----------------------
text = "X-DSPAM-Confidence:    0.8475"

# Usar rfind para encontrar el espacio idicado
pos = text.rfind(' ')

# se usa en un espacio  indicado y quitar espacios inecesarios 
number_str = text[pos:].strip()

# cadena flotante
number_flotante = float(number_str)

# Ver el número flotante
print(number_flotante)




















