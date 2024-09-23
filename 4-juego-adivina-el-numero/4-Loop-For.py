# los loop for con bucles que se repiten una cantidad definida de veces.


#necesitas un objeto iterable para poder pasar por cada uno de sus elementos
lista = ['a','b','c','d']

for letra in lista:#letra es una variable inventada para el loop
    numero_letra = lista.index(letra)+1 #tambien podemos indexar el loop, para que muestre en que posicion esta cada letra
    print(f'Letra {numero_letra}: {letra}')


#otro ejemplo

lista = ['pablo','laura','fede','luis','julia']

for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('este no empieza con L')
    
    
#otro ejemplo

numeros = [1,2,3,4,5,6]
mi_valor= 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)   

#otro ejemplo
palabra= 'python'

for letra in palabra:
    print(letra)

    
