from pathlib import Path

carpeta = Path('C:/Users/franco/Desktop/mis-proyectos/curso-python/6-recetario/prueba.txt')

#como podemos ver, pathlib es parecido a os. pero no hace falta hacer un close, y demas, es mucho mas simple


print(carpeta.read_text()) #lee el archivo

print(carpeta.name) #lee el nombre del archivo

print(carpeta.suffix) #nos da el tipo de archivo , en este caso txt

print(carpeta.stem) #nos da el nombre sin el sufijo

#tambien podemos chequear si el archivo existe
if not carpeta.exists():
    print('este archivo no existe')
else: 
    print('genial este archivo existe')

#ademas podemos modificar el archivo, sin tener que cambiar el modo de solo lectura, solo write o sin cerrar o abrir como en os


