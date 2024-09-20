#trabajas en una empresa, y los vendedores reciben el 13% de las ventas, el programa pedira el total de ventas y calculara cuanto le corresponde de comision

NombreVendedor = input('cual es su nombre? ')

TotalVentas = input('ingrese el total de ventas que obtuvo: ')
TotalVentas = int(TotalVentas)

comision = TotalVentas * 13 / 100

print(f'hola {NombreVendedor}, la comision que te corresponde segun el total de ventas es {comision}')

