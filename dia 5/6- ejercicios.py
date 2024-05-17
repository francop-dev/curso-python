'''from random import * EJERCICIO 1

dado1 = [1, 2, 3, 4, 5, 6]
dado2 = [1, 2, 3, 4, 5, 6]

def lanzar_dados(lista1, lista2):
    resultado_dado1 = choice(lista1)
    resultado_dado2 = choice(lista2)
    return resultado_dado1, resultado_dado2

def evaluar_jugada(resultado):
    suma_dados = sum(resultado)
    if suma_dados <= 6:
        print(f'La suma de tus dados es {suma_dados}. Lamentable')
    elif suma_dados >= 6 and suma_dados <= 10:
        print(f'La suma de tus dados es {suma_dados}. Tienes buenas chances')
    elif suma_dados > 10:
        print(f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora')

resultado_dados = lanzar_dados(dado1, dado2)
print("Resultados de los dados:", resultado_dados)
evaluar_jugada(resultado_dados)
'''
"""EJERCICIO2
lista_numeros = [1,2,15,7,2]

def reducir_lista(lista):
    lista_sin_repetidos = list(set(lista))
    numero_max = max(lista_sin_repetidos)
    lista_sin_repetidos.remove(numero_max)
    return lista_sin_repetidos


def promedio(lista):
    lista_suma = sum(lista)
    lista_promedio = lista_suma / len(lista)
    return lista_promedio


resultado = reducir_lista(lista_numeros)
resultado_total = promedio(resultado)

"""
from random import *

def lanzar_moneda():
    resultados = ['cara','cruz']
    resultado = choice(resultados)
    return resultado


lista_numeros= [1,2,3,4,5,6,7]

def probar_suerte(moneda,lista):
    if moneda == 'cara':
        print('La lista se autodestruirá')
        return []
        
    elif moneda == 'cruz':
        print('La lista fue salvada')
        return lista
        
    
resultado_total = lanzar_moneda()
print(resultado_total)

resultado_lista = probar_suerte(resultado_total,lista_numeros)
