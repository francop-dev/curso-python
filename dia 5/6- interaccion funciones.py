from random import shuffle
#lista inicial
palitos = ['-','--','---','----']



#mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista




#pedirle al usuario que elija
def probar_suerte():
    intento = ''
    
    while intento not in ['1','2','3','4']:
        intento = input('elige un numero del 1 al 4: ')
    return int(intento)




#comprobar intento
def chequear_intento (lista,intento):
    if lista [intento - 1] == '-':
        print('A lavar los platos')
    else:
        print('esta vez te has salvado')
        
    print(f'te ha tocado {lista[intento-1]}')
    
    
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)