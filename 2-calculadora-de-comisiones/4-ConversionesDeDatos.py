"""podemos cambiar un int a un float o un str a un int como queramos 
python tambien nos cambia valores automaticamente, esto se llama forma implicita
y si cambiarmos nosotros el tipo de dato se llama explicita"""

#ejemplo float y int

num1 = 20

num2 = 30.5

#conversion explisita

consuta_edad = input('dime tu edad: ')
print(type(consuta_edad))#aca es un str

consuta_edad = int(consuta_edad)

print(type(consuta_edad))#aca es un int

edad_siguiente = consuta_edad + 1.2

print(type(edad_siguiente))#aca es un float