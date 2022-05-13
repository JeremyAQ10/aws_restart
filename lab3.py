mystring = "This is a string."
print(mystring)

print(type(mystring))
print(mystring + " is of the type " + str(type(mystring)))

#concatenación de cadenas
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
print(firstString + secondString)
print(f"{firstString} is of data type  {type(firstString)}")
print(firstString, "is of data type",str(type(firstString)))

name = input("what is your name? ")
print(name)

color = input("cual es tu color favorito? ")
animal = input("cual es tu animal favorito? ")
print("{}, you like a {} {}!".format(name,color,animal))
print(f"{name} le gusta un {color} {animal}")