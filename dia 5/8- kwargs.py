#la diferencia entre los args comunes es que los kwargs pueden contener nombres de cada argumento indefinido que tengamos, de esta manera podemos obtener el item completo, el nombre o el valor

'''def suma (**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total

print(suma(x=3,y=5,z=2))

EJERCICIO 2
def lista_atributos(**kwargs):
   lista_valores=[]
   for claves,valores in kwargs.items():
       lista_valores.append(valores)
   return lista_valores
   
    
kwargs = {'x':'uno','y':'dos','z':'tres'}

resultado = lista_atributos(**kwargs)    
print(resultado)    
'''
'''
EJERCICIO 3
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")

# Ejemplo de uso
describir_persona("María", color_ojos="azules", color_pelo="rubio")
    |   |   |   |   23

'''