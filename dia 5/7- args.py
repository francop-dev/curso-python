#las funciones no pueden contener argumentos con numeros indefinidos, tiraran error. por eso estan los argumentos indefinidos (*args) y **kwargs
 
def suma (*args):
    total = 0
    
    for arg in args:
        total += arg
    return total

print(suma(1,5,1,20,30,50))#aca podemos sumar cual numero sea que no tirara error.

#tambien podemos hacerlo de forma mas simple

def suma1 (*args):
    
    return sum(args)

print(suma1(1,2,6,8))

'''practicas'''


#sumar todas las potencias de cada numero    
def suma1(*args):
    return sum(x**2 for x in args)

print(suma1(1, 51, 51, 20, 61, 84))


#pasar cada numero negativo a positivo y sumarlos
def suma_absolutos (*args):
    
    return sum(abs(x)for x in args)
    
print(suma_absolutos(1,-2,-6,8))

#funcion que recibe nombre y numeros indefinidos
def numeros_persona (nombre, *args):
    nombre = 'Federico'
    return print(f'{nombre}, la suma de tus numeros es {sum(args)}')

print(numeros_persona(75,20,65))