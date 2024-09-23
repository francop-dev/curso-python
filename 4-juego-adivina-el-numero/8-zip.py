#zip combina 2 o mas listas y los hace una lista de tuples y los pone en orden

nombres = ['ana','hugo','valeria']
edades = [65,29,42] #siempre va a juntar de a pares, va a llegar a la lista mas corta
ciudades = ['lima','peru','mexico']
combinados = list(zip(nombres,edades,ciudades))

print(combinados)

#podes crear un loop que contenga todos los elementos que juntamos

for nombre,edad,ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')