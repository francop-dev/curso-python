#tenemos mas formas de interactuar con las listas, una es con los loops

palabra = 'python'

lista = [letra for letra in palabra] #esto metio a 'python' dentro de una lista

print(lista)

#tambien pdemos trabajar con valores numericos

lista = [n for n in range(0,21)]
print(lista)


#y tambien podemos modificar con operadores

lista = [n/2 for n in range(0,21)]
print(lista)

#tambien podemos tener if
lista = [n if n*2 > 10
         else 'no' for n in range(0,21) ]
print(lista)

#supongamos que tenemos una lista de medidas en pies, y quiero pasarlo a metros

pies = [12,32,34,56,67]
metros = [n/3.281 for n in pies]
print(metros)