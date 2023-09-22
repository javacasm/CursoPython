# Solución 1 - Ajedrez con cadenas y su operador *

base_par = '# '
base_impar = ' #'
linea_par = base_par * 8 
linea_impar = base_impar * 8 
tablero = (linea_par + '\n' + linea_impar + '\n' ) * 4

print(tablero)

# Solución 2 - Ajedrez con bucle for

for i in range(8):
    if i%2 == 0 : # es par
        print(linea_par)
    else:
        print(linea_impar)