#los diccionarios tienen un conjunto de palabra clave y un valor, las palabras claves no pueden repetirse, los valores si

mi_dic = {'c1':'valor1'} #c1 es la clave q no se puede repetir

#una buena manera de usar un diccionario puede ser para bases de datos por ej, donde la podes buscar tanto la clave como el valor

diccionario = {'c1':'valor1','c2':'valor2','c3':'valor3'}

print(diccionario)

resultado = diccionario['c1'] #aca nos dara el valor de la clave 
print(resultado)

cliente= {'nombre':'juan','apellido':'fuentes','peso':70,'talla':1.87}

consulta = (cliente['apellido'])

print(consulta)

#tambien podemos tener una lista dentro de un diccionario

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':23,'s2':43,'s3':90}}

print(dic['c2'][1]) # aca vemos como buscar dentro de la lista que esta dentro del diccionario

print(dic['c3']['s2']) # aca buscamos en un diccionario dentro de otro diccionario

#vamos a ver como imprimir valores y cambiarlos (no las claves)
dic1 = {'c1':['a','b','c'],'c2':['d','e','f']}

resultado = dic1['c2'][1]

imprimir = print(resultado.upper()) #logramos imprimir la E en mayusculas

#modificar o agregar valores en diccionarios
dic2 = {1:'a',2:'b'}
print(dic2)

dic2[3] = 'c'
print(dic2)

dic2[2] = 'B'
print(dic2)

#como conocer todas las claves de un diccionario
print(dic.keys())

#como conoces los valores de un diccionario
print(dic.values())

#todos los valores incluidos keys y values
print(dic.items())


