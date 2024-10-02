from random import *

#por primera vez importamos metodos a python, en este caso random, y utilizaremos randint

aleatorio = randint(1,50)
print(aleatorio)

#uniform, nos da un valor decimal, es decir:
aleatorio = uniform(10,12)

print(aleatorio)

#random elije un numero decimal entre 0 y 1
aleatorio = random()
print(aleatorio)

#choice sirve para una eleccion aleatorio dentro de una lista
colores = ['azul','rojo','verde','amarillo']
aleatorio = choice(colores)
print(aleatorio)

#shuffle es mezclar, puedes mezclar por ejemplo una lista
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)

