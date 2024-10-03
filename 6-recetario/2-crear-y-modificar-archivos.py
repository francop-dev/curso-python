mi_archivo = open(r'C:\Users\franco\Desktop\mis-proyectos\curso-python\6-recetario\prueba.txt','w')

#la 'r' es solo para leer
#la 'w' sobre escribe y borra todo lo que tenga 
#la 'a' empieza a escribir al final del texto existente (es el mas usado talvez)


#para escribir y sobre escribir(es decir se borra lo q habia en el texto y se escribe lo siguiente, ademas cuando damos el open utilizamos 'w')
'''mi_archivo.write(hola 
                 amigos
                 como 
                 estan

#este metodo concatena todos los strings que pongamos, no se utiliza mucho
mi_archivo.writelines(['hola','mundo','aqui','estoy'])

for p in lista:
    archivo.writelines(p + '\t')

mi_archivo.close()'''

mi_archivo = open('registro.txt','w')


registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

for p in registro_ultima_sesion:
    mi_archivo.writelines(p + '\t')

mi_archivo = open('registro.txt','r')

print(mi_archivo.read())
