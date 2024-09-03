#los strings son inmutables, si se pueden concatenar


n1 = 'kari'
n2 = 'na'

print(n1+n2)

#tambien se pueden multiplicar

print(n1*5)

#tambien pueden tener varias lineas de codigo

poema = '''Mil pequeños peces blancos 
como si hirviera
el color del agua'''

print(poema)

#tambien podemos preguntar si existen ciertos caracteres, nos dara un valor booleano

print('agua' in poema) #chequea si esta y da True

print('agua' not in poema) # chequea que no este y da False porque si esta

#contar el largo de los string

print(len(poema))