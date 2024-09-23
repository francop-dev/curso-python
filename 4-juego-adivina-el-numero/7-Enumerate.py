#el enumerate sirve para acceder a los indices de una operacion

lista = ['a','b','c']


for item in enumerate(lista):
    print(item)
    

#podemos hacer un indice    
for indice,item in enumerate(lista):
    print(indice,item)
    
    
#tambien lo podemos usar afuera de un loop

mis_tuples = list(enumerate(lista))    
print(mis_tuples[1][0])

