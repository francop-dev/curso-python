#path puede crear rutas con listas de strings

from pathlib import Path

base = Path.home() #nos dirije al directorio principal del usuario que estemos usando en el momento, en este caso c:/users/franco

guia = Path(base,'europa','españa',Path('barcelona','sagrada_familia.txt')) #si concatenamos base a esas palabras, tendremos una ruta absoluta

guia2 = guia.with_name('La_Pedrera.txt') #con el metodo with_name podemos copiar la ruta pero cambiar el archivo seleccionado

#tambien podemos acceder al la carpeta que contiene el archivo con el metodo parent
print(guia.parent)

#y en vez de utilizar .parent muchas veces si queremos navegar muchas carpetas atras, podemos usar esto
print(guia.parents[2]) #es el equivalente a usar parent 3 veces

#es decir, path admite cadenas como mismos objetos creados con path 

print(guia)
print(guia2)

#muy bien, supongamos que tenemos una carpeta que tiene subcarpetas, en este caso se llama europa, contiene francia y españa y dentro ciudades y dentro de esas archivos txt.

ruta = Path(Path.home(),'Europa')

for txt in Path(ruta).glob('*.txt'): #este for, nos dara como resultado los archivos .txt (* significa todos) que tengamos en la carpeta europa.
    print(txt)
    
for txt in Path(ruta).glob('**/*.txt'): # si usamos **/* , nos dara todos los archivos .txt que se aniden en todas las sub carpetas que tenga europa
    print(txt)