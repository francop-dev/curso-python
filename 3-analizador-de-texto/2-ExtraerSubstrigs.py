#es parecido al metodo index, pero en ves de extraer un solo carater, podemos extraer varios, consecutivamente o no

#extraccion de varios caracteres

texto = 'ABCDEFGHI'

fragmento = texto[2:5] #extrae desde el indice 2 (C) hasta el 5 (D) pero no lo incluye.

print(fragmento)


texto1 = 'hoy es un buen dia'

fragmento1 = texto1[2:15:2]

print(fragmento1)