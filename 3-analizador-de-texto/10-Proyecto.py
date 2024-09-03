
texto = input('ingresa un texto: ')

python = texto.find('python')

print('muy bien, ahora ingresa 3 letras a tu eleccion')

primeraletra = texto[0]
ultimaletra = texto[-1]

letra1 = input('ingresa la primer letra: ')
letra2 = input('ingresa la segunda letra: ')
letra3 = input('ingresa la segunda letra: ')

resultadoletra1 = texto.count(letra1)
resultadoletra2 = texto.count(letra2)
resultadoletra3 = texto.count(letra3)

texto = texto.lower()
texto = texto.split()
resultadotexto = len(texto)


print(f'tu primera letra aparece {resultadoletra1} veces')
print(f'tu primera segunda aparece {resultadoletra2} veces')
print(f'tu primera tercera aparece {resultadoletra3} veces')

print(f'tu texto tiene {resultadotexto} palabras.')

print(f'la primera letra de tu texto es {primeraletra} y la ultima es {ultimaletra}')

texto.reverse()
print(f'tu texto el revez estaria de esta manera: {texto}')

if python == -1:
    print('"python" no esta en tu texto')
else:
    print('"python" esta en tu texto')