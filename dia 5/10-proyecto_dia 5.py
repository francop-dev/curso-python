from random import choice

vidas = 6
palabras = ('casa', 'burro')

def elegir_palabra():
    palabra = choice(palabras)
    cantidad_letras = len(palabra)
    palabra_oculta = '_' * cantidad_letras
    print(f'La palabra que debes adivinar es: {palabra_oculta} ({cantidad_letras} letras)')
    return palabra, palabra_oculta

def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    nueva_palabra_oculta = ''.join([letra if palabra[i] == letra else palabra_oculta[i] for i in range(len(palabra))])
    return nueva_palabra_oculta

def pedir_letra(palabra, palabra_oculta, vidas):
    while vidas > 0 and '_' in palabra_oculta:
        elegir = input('Elige tu letra: ')
        if elegir in palabra:
            print('Correcto')
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, elegir)
        else:
            vidas -= 1
            print(f'Incorrecto, te quedan {vidas} vidas')
        
        print(f'La palabra que debes adivinar es: {palabra_oculta}')
        
        if '_' not in palabra_oculta:
            print('¡Felicidades! Has adivinado la palabra.')
            break
        if vidas == 0:
            print('¡Juego terminado! Te has quedado sin vidas.')
            break
    return elegir

# Seleccionar una palabra
palabra_selecta, palabra_oculta = elegir_palabra()

# Pedir letras en un bucle hasta que se acaben las vidas o se adivine la palabra
pedir_letra(palabra_selecta, palabra_oculta, vidas)


