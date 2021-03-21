import os 

def fileWordCounter(nombre_fichero):
    file = open(nombre_fichero, "rt")

    numero_lineas = 0
    numero_palabras = 0
    numero_caracteres = 0
    
    for lineaRaw in file:
        linea = lineaRaw.strip('\n') # no contaremos el fin de línea como caracter 

        palabras = linea.split() # Lista de palabras
        numero_lineas += 1
        numero_palabras += len(palabras)
        numero_caracteres += len(linea)

    file.close()

    return numero_lineas, numero_palabras, numero_caracteres


print('Revisando directorio '+os.getcwd())
print('Fichero;líneas;palabras;caracteres;')
for fichero in os.listdir():
    try:
        if os.path.isfile(fichero) and  fichero.endswith('.py'):
            nLineas,nPalabras,nCaracteres = fileWordCounter(fichero)
            print('"{}";{};{};{};'.format(fichero,nLineas,nPalabras,nCaracteres ))
    except:
        pass
        # print('Error con ',fichero)

    