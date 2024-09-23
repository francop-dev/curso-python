#el loop while toma como limite de repeticiones una condicion

#por ej las vidas en un juego, si tenes 3 vidas seguis jugando hasta que tengas 0

#un elemento muy importante en los loops son : break, pass y continue

monedas = 5

while monedas > 0:
    print(f'tengo {monedas} monedas')
    monedas = monedas - 1
else: print('no tengo mas monedas')

#otro ejemplo

'''respuesta = 's'

while respuesta == 's':
    respuesta = input('quieres seguir? (s/n)')
else: 
    print('gracias ')'''
    
#pass
'''valor = 10

while valor == 10:
    pass''' #el pass hace que el programa no continue ni se pueda reiniciar
    
print('hola')    

#break
nombre = input('tu nombre: ')

for letra in nombre:
    if letra == 'r':
        break
    print(letra)

#continue 
#es parecido a el break pero no rompe el el loop, sino que continua con los demas parametros
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)