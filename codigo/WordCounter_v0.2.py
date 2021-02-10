# TODO: errores si no es un fichero o permisos
def fileWordCounter(nombre_fichero):
    file = open(nombre_fichero, "r")

    numero_lineas = 0
    numero_palabras = 0
    numero_caracteres = 0
    for lineas in file:
        lineas = lineas.strip("\n") # no contaremos el fin de línea como caracter 

        palabras = lineas.split() # Lista de palabras
        numero_lineas += 1
        numero_palabras += len(palabras)
        numero_caracteres += len(lineas)

    file.close()

    return numero_lineas,numero_palabras,numero_caracteres

import os 
ficheros = os.listdir() 
print('Fichero;lineas;palabras;caracteres:')
for fichero in ficheros:   
    try:
        nLineas,nPalabras,nCaracteres = fileWordCounter(fichero)
        print('"{}";{};{};{};'.format(fichero,nLineas,nPalabras,nCaracteres ))
    except:
        print('Error con ',fichero)

    