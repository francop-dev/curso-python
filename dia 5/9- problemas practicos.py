#1
#crea una funcion llamada 'devolver_distintos() que reciba 3 intergers como parametros
#si la suma de los 3 nmeros es mayor a 15, va a devolver el numero mayor.
#si la suma de los 3 numeros es menor a 10, va a devolver el numero menor.
#si la suma de los numeros es es un valor entre 10 y 15 (incluidos) va a devolver el numero de valor intermedio.
'''
def devolver_distintos(*args):

    
    total = sum(args)
    numeros_ordenados = sorted(args)
    valor_intermedio = numeros_ordenados[1]
    if total > 15:
            print(f'el numero mayor es {max(args)}')
    elif total < 10:
            print(f'el numero menor es {min(args)}')
            
    elif total >= 10 and total <= 15:
            print(f'el numero intermedio es {valor_intermedio}')
        

devolver_distintos(1,3,2)
'''
#2
#Escribe una función (puedes ponerle cualquier nombre que
#quieras) que reciba cualquier palabra como parámetro, y que
#devuelva todas sus letras únicas (sin repetir) pero en orden
#alfabético.
#Por ejemplo si al invocar esta función pasamos la palabra
#"entretenido", debería devolver ['d','e','i','n','o','r','t']
'''
def palabras (*args):
    definir = []
    for arg in args:
        definir = set(arg)
    return print(sorted(definir))
        
palabras('ejemplo')
'''
#3 
# Escribe una función que requiera una cantidad indefinida de
#argumentos. Lo que hará esta función es devolver True si en
#algún momento se ha ingresado al numero cero repetido dos
#veces consecutivas.

'''def dos_ceros_consecutivos(*args):
    # Iterar sobre los argumentos con sus índices
    for i in range(len(args) - 1):
        # Comprobar si el actual y el siguiente son ceros
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False
            

funcion(0,2,5,4,2,1,5,0,0,1,2,5)'''

#4
'''Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.'''
def contar_primos(numero):
    
    primos = [2]
    iteracion = 3
    
    if numero < 2:
        return 0
    while iteracion <= numero:
        for n in range(3,iteracion,2):
            
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion +=2
    print(primos)
    return len(primos)

print(contar_primos(50))
    