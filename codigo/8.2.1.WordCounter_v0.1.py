# Fichero quijote.txt de https://gist.github.com/jsdario/6d6c69398cb0c73111e49f1218960f79

nombre_fichero = 'codigo/data/el_quijote.txt'

file = open(nombre_fichero, 'rt', encoding="utf8") # Abrimos el fichero en modo lectura de texto, usando una codificación estándar

numero_lineas = 0
numero_palabras = 0
numero_caracteres = 0

for lineaRaw in file: # va a recuperar línea a línea el contenido del fichero
    linea = lineaRaw.strip('\n') # no contaremos el fin de línea como caracter 

    palabras = linea.split() # Lista de palabras
    numero_lineas += 1
    numero_palabras += len(palabras) 
    numero_caracteres += len(linea)

file.close()

# formato antiguo
print('"{}" {} {} {} '.format( 
    nombre_fichero, numero_lineas, numero_palabras, numero_caracteres))
# usando f-string    
# print(f'"{nombre_fichero}" {numero_lineas} {numero_palabras} {numero_caracteres}')
    