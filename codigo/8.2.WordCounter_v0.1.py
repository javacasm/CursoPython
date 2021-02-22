# Fichero quijote.txt de https://gist.github.com/jsdario/6d6c69398cb0c73111e49f1218960f79

nombre_fichero = 'el_quijote.txt'
file = open(nombre_fichero, 'rt') # Abrimos el fichero en modo lectura de texto

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

print('"{}" {} {} {} '.format(nombre_fichero,
                              numero_lineas, numero_palabras, numero_caracteres))

    