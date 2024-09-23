from random import *

#valores
vidas = 8
numero_adivinar = randint(0,101)
print(numero_adivinar)
print(type(numero_adivinar))


nombre = input('bienvenido al juego de adivinar el numero! cual es tu nombre? ')

print(f'muy bien {nombre}, eh pensado un numero entre el 0 y el 100, tendras 8 intentos para adivinar!')

ingreso = input('cual numero ingresaras? ')
if ingreso != int:
    print('ingresa un numero!, no una letra!!')
while vidas > 1:
    ingreso = int(ingreso)
    if ingreso > 100 or ingreso < 0:
        vidas -=1
        print(f'ese no es un numero valido! te quedan {vidas} vidas! ')
        ingreso = input('ingresa otro numero: ')
    elif ingreso > numero_adivinar:
        vidas -= 1
        print(f'te pasaste! el numero es mas bajo, ahora tienes {vidas} vidas!')
        ingreso = input('ingresa otro numero: ')
    elif ingreso < numero_adivinar:
        vidas -= 1
        print(f'es muy bajo! el numero es mas alto, ahora te quedan {vidas} vidas!')
        ingreso = input('ingresa otro numero: ')
    elif ingreso == numero_adivinar:
        print(f'Ganaste {nombre}, te quedaron {vidas} vidas!')
        break
else:
    print(f'perdiste {nombre}!')