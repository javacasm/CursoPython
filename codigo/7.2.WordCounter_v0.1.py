
nombre_fichero = '0.0.Indice.md'
file = open(nombre_fichero, 'r')

numero_lineas = 0
numero_palabras = 0
numero_caracteres = 0
for lineas in file:
    lineas = lineas.strip('\n') # no contaremos el fin de línea como caracter 

    palabras = lineas.split() # Lista de palabras
    numero_lineas += 1
    numero_palabras += len(palabras)
    numero_caracteres += len(lineas)

file.close()

print('"{}";{};{};{};'.format(fichero,numero_lineas,numero_palabras,numero_caracteres))

    