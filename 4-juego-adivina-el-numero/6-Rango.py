#range sirve para no tener que especificar hasta donde puede llegar tu loop

#en vez de hacer una lista:
lista = [1,2,3,4,5,6,7]

#haces un range:
lista = range(7) #el indice indica donde va a parar, es decir cuenta hasta 6
lista = range(10,20)#indicamos desde donde contar hasta donde, en este caso de 10 a 20
lista = range(10,20,2) #el tercer numero indica de a cuantos contar, es decir iria 20,22,24,26,etc

for numero in lista:
    print(numero)