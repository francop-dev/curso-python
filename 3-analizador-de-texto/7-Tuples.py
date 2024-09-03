#los tuples son parecidos a las listas, pero son inmutables, ocupan menos espacios de memoria y es a prueba de daños

mi_tuple = (1,2,3,4,5)

#se pueden utilizar el metodo index

print(mi_tuple[0])

 #se puede contener un tuple dentro de otro tuple
 
mi_tuple = (1,2,(10,20),4)

print(mi_tuple[2][0])

#netodos tuples

t= (1,2,3,1)

print(t.count(1))

