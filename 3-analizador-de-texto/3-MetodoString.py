

#existen 6 metodos mas para modificar strings, teniamos index y format. los siguientes son:

texto = 'Hola Amigos Como Estan'


ej1 = texto.upper() #pasar a mayusculas
ej2 = texto[2].upper() #pasar a mayuscula solo el indice 2
print(ej1,ej2)

ej1 = texto.lower() #pasar a minusculas
ej2 = texto[2].lower() #pasar a minuscula solo el indice 2
print(ej1 , ej2)

ej1 = texto.split() #separar en partes (lista)
ej2 = texto.split('t') #va a separar el texto por cada delimitador, en este caso es la t, el texto estaria dividido en 2
print(ej1,ej2)

texto.join #unir items usando separador
a='vamos'
b='boquita'
c='carajo'
d= ' '.join([a,b,c])
print(d)

ej1 = texto.find('texto')#encontrar sub-string (parecido a index, va a dar el indice donde empieza)
print(ej1)

ej2 = texto.replace('a','x')#reemplazar un substring osea un caracter, el primer termino es el remplazado x el segundo
print(ej2)


texto = 'Si la implementación es difícil de explicar, puede que sea una mala idea.'
texto1 = texto.replace('difícil','fácil')
resultado = texto1.replace('mala','buena')
print(resultado)