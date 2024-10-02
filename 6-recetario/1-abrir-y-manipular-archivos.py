




mi_archivo = open(r'C:\Users\franco\Desktop\mis-proyectos\curso-python\6-recetario\prueba.txt')

'''
una_linea = mi_archivo.readline()
print(una_linea.upper())
linea_dos = mi_archivo.readline()
print(linea_dos)
linea_tres = mi_archivo.readline()
print(linea_tres)'''



'''for l in mi_archivo:
    print('aqui dice: ' + l)'''
    
    
todas = mi_archivo.readlines()
todas = todas.pop()

print(todas)