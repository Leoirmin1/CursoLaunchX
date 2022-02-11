from datetime import date #Importamos una libreria para el tiempo

# Operaciones en python

sum = 1 + 2      
product = sum * 2
print(product)

# Mostrar tipo de dato de una variable

distancia_a_alfa_centauri = 4.367
print(type(distancia_a_alfa_centauri))

# Manejo de fechas en python

print(date.today()) # Imprimimos la fecha actual

# Conversion de tipo de datos

print("Today's date is: " + str(date.today()))

# Recopilar datos

print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre")
print("Saludos: " + name)

# Trabajar con numeros

print("Calculadora")
first_number = input("Primer numero:")
second_number= input("Segundo numero:")
print( first_number + second_number) # Como es una cadena de texto se concatena
print(int(first_number) + int(second_number)) # Convertimos a enteros y se suma