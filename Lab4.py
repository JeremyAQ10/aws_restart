#demostración de una lista

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

myFruitList[2] = "orange"


print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

print(myFruitList)

#Demostración de una tupla
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#Demostración de un diccionario
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
print(myFavoriteFruitDictionary.keys())
print(myFavoriteFruitDictionary.items())

print(list(myFavoriteFruitDictionary.keys()))
print(list(myFavoriteFruitDictionary.values()))








