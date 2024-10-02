precios_cafe = [('capuccino',1.5),('expresso',1.2),('moka',1.9)]

#como saber cual tiene el precio mayor?
def cafe_mas_caro(lista_precios):
    
    precio_mayor = 0
    cafe_mas_caro = ''
    
    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    
    return (cafe_mas_caro,precio_mayor)

#este no seria posible sin un tupple con un dato y un valor ("capuccino",1.5)
cafe , precio = cafe_mas_caro(precios_cafe)
print(f'el cafe mas caro es {cafe} cuyo precio es {precio}')