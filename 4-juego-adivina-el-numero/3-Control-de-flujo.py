# los operadores de control de flujo son ,if, elif y else


#if
numero1 = 1
numero2 = 2

if numero2 > numero1:
    print('numero 2 es mayor')
    
    
#elif es solo como un if mas abajo del if
#es como una segunda verificacion

mascota = 'perro'

if mascota == 'gato':
    print('tienes un gato')
elif mascota == 'perro':
    print('tienes un perro')
else: # else es la ultima verificacion que hace el programa, no podes poner otro if despues o otro elif
    print('no tienes mascotas') 