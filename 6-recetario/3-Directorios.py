#import os es una forma que tiene python para encontrar rutas hacia archivos

import os 

ruta = os.getcwd() #este metodo significa current work directory (obtenes directorio actual)

print(ruta)

ruta = os.chdir('c://Users//franco//Documents') #change directory, es decir cambiar la ruta distinta de trabajo, es decir abrir un archivo de otro lugar 

ruta = os.makedirs('C://Users//franco\Desktop//mis-proyectos//curso-python//6-recetario//nueva-carpeta') #con makedirs podes crear una carpeta nueva


ruta = 'C://Users//franco//Desktop//mis-proyectos//curso-python//6-recetario'

elemento = os.path.basename(ruta) #si queres obtener el nombre del archivo de nuestra ruta (la ultima parte)
print(elemento)

elemento = os.path.dirname(ruta) #y si queremos obtener la ruta principal, es decir donde se aloja el archivo
print(elemento)

elemento = os.path.split(ruta) #esto nos trae toda la ruta pero en una tupla
print(elemento)

#como eliminar carpetas?
os.rmdir('C://Users//franco\Desktop//mis-proyectos//curso-python//6-recetario//nueva-carpeta')

#otra forma de obtener rutas de archivos

from pathlib import Path

carpeta = Path('c:/Users/franco/Documents')
archivo = carpeta / 'texto1.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())