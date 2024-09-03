
#las listas pueden tener todo tipo de datos, y varios tipos de datos al mismo tiempo y si son inmutables, no como los strings
#a continuacion un ejemplo

numeros = [12,23,43,54,6,'t','hola','chorizo']

print(len(numeros)) #se puede ver el largo de los elementos de una lista

print(numeros[0]) #podemos indexar
print(numeros[0:4])
print(numeros[0:4:2])

#concatenar

numeros2 = [123,24,23,23]

print(numeros+numeros2) # se unieron ambas listas


#podemos sobreescribir una lista

numeros[2] = 'chorizin'
print(numeros)

#tenemos muchos tipos de metodos para afectar a las listas

'''append'''
numeros.append('g') #agregamos la g en el final
print(numeros)

'''pop'''
hola = numeros.pop(2) # elimina el elemento que elijamos por index,podemos guradarlo en una variable
print(hola)

'''sort'''
solonumeros = [1,2,5,6,8,4,6,2,3]
solonumeros.sort() #ordena todo en forma ascendente, numeros o letras inclusive pero no mezcladas
print(solonumeros)

'''reverse'''
solonumeros.reverse()
print(solonumeros)