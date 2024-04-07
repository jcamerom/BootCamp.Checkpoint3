# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
testString = 'Hola'
testNumber = 4
testList = [1, 'number', True , ['ahora', 2]]
testBoolean = True

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.
firstLetter = testString[0]
secondLetter = testString[1]
thirdLetter = testString[2]
frag_3_first_letters = firstLetter + secondLetter + thirdLetter
print(frag_3_first_letters)

# Exercise 3: Use an index to grab the first element from your list.
firstList = testList[0]
print(firstList)

# Exercise 4: Create a new number variable that adds 10 to your original number.
newNumber = testNumber + 10
print(newNumber)

# Exercise 5: Use an index to get the last element in your list.
lastList = testList[-1]
print(lastList)

# Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
listNames = names.split(',')
print(listNames)

# Exercise 7: Get the first word from your string using indexes. Use the upper function 
# to transform the letters into uppercase. Create a new string that takes the uppercase word and 
# the rest of the original string.
sentenceString = testString + ' que tal'
print(sentenceString)

firstWordUser = sentenceString.split()
firstWord = firstWordUser[0].upper()
newSentence = firstWord + sentenceString.lstrip('Hola')
print(newSentence)

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
interpolationExample = f'Mi numero elegido es: {testNumber}'
print(interpolationExample)

# Exercise 9: Print “hello world"
print('"hello world"')

# Exercise 10: Además necesito que me crees una cadena que contenga la palabra "Hola". Usando la palabra clave en el 
# método de búsqueda o el índice, busque y seleccione "Hola" en su cadena. Y usando la función de reemplazo, 
# reemplace "Hola" en su cadena con "adiós".
miCadena = "Hola amigos"
print(miCadena)
print(miCadena.replace('Hola', 'Adios'))


