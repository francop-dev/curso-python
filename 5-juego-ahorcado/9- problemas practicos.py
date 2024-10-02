#devolver distintos

def devolver_distintos (*args):
    numeros = sum(args)
    lista = sorted(args)
    print(lista)
    valor_mas_bajo = lista[0]
    valor_mas_alto = lista[2]
    valor_medio = lista[1]

        
    if numeros > 15:
            print(valor_mas_alto)
    elif numeros < 10:
            print(valor_mas_bajo)
    elif 10 <= numeros <=15 :
            print(valor_medio)
            
devolver_distintos(5,3,4)
            
