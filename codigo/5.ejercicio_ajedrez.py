# tablero de ajedrez

print('+----------------+')  # linea de arriba del marco del tablero
for j in range(8):
    linea = '|'  # marco vertical de la izda

    for i in range(8): # hacemos diferentes las lineas pares e impares
        if j%2==0: # es par
            linea+='# '
        else:  # es impar
            linea+=' #'
    linea += '|' # marco vertical de la drcha
    print(linea)
print('+----------------+')  # linea de abajo del marco del tablero
