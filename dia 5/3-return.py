#return sirve para que la funcion devuelva un resultado y el mismo pueda ser guardado en una variable

def sumar(num1,num2):
    return num1+num2

resultado = sumar(1,2)
print(resultado)

def multiplicar (num1,num2):
    return num1*num2

resultado1 = multiplicar(2,200)
print(resultado1)

#dar vuelta una palabra y hacerla mayuscula mediante una funcion
def invertir_palabra(palabra):
  palabra_invertida = palabra[::-1].upper()
  return palabra_invertida
    
palabra = input('ingrese la palabra que quiera dar vuelta y poner en mayusculas ')
resutado = invertir_palabra(palabra)
print(resutado)
