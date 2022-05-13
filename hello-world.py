myValue = 3.14

# type() muestra el tipo de dato de lo que esté dentro de los paréntesis
print(type(myValue))

# castear/transformar valor numérico a texto
print(str(myValue) + " es del valor " + str(type(myValue)))

#Variable se modifica con valor imaginario (complejo)
myValue = 5j

print(myValue)

# type() muestra el tipo de dato de lo que esté dentro de los paréntesis
print(type(myValue))

# castear/transformar valor numérico a texto
print(str(myValue) + " es del valor " + str(type(myValue)))

# Variable se modifica a valor booleano
myValue = True
myValue2 = False

print(myValue)
print(myValue2)

# castear/transformar valor booleano a texto
print(str(myValue2) + " es del valor " + str(type(myValue2)))

# Formateo de strings en Python con f-strings
print(f"{myValue2} is of data type {type(myValue2)} ")

# castear/transformar valor booleano a numero
print(int(myValue)) # True - 1
print(int(myValue2)) # False - 0
