#funcion que chekee si un numero tiene mas de 3 cifras
def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado= chequear_3_cifras(123)
print(resultado)

#con for
def dale_una_mas(lista):
    lista_3_cifras = []
    lista_menos = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else: 
            lista_menos.append(n)
    return lista_3_cifras,lista_menos
resultado = dale_una_mas([25,12022,232])
print(resultado)

lista_numeros = [132,242,133,125,205,204]

def cantidad_pares(lista_numeros):
    suma=[]
    for n in lista_numeros:
        if n%2 == 0:
            suma.append(n)
        else:
            pass
    return suma
resultado = cantidad_pares(lista_numeros)
print(resultado)

lista_numeros = [1,50,502,5000,755,600,33,61]
 
def cantidad_pares(lista_numeros):
    cantidad=0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad += 1
        else:
            pass
    return print(cantidad)


lista_numeros = [1,52,90,850,5511]


lista_numeros = [12,13,14,15,16,17,18]

def cantidad_pares(lista_numeros):
    pares = 0
    for n in lista_numeros:
        if n % 2 == 0:
            pares += n
        else:
            pass
    print (pares)
cantidad_pares(lista_numeros)