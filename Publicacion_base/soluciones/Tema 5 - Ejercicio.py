# Solución 1 - Ajedrez con cadenas y su operador *

base_par = '# '
base_impar = ' #'
linea_par = base_par * 8 
linea_impar = base_impar * 8 

print('Tablero de ajedrez\n')

tablero = (linea_par + '\n' + linea_impar + '\n' ) * 4

print(tablero)

# Solución 2 - Ajedrez con bucle for

print('\nTablero de ajedrez con bulce for\n')

for i in range(8):
    if i % 2 == 0 : # es par
        print(linea_par)
    else:
        print(linea_impar)

# Solución triángulo - usando operador *

print('\nTriángulo\n')

for i in range(10):
    print('*' * i)

# Solución árbol

N = 10

print('\narbolito\n')

for i in range(1,N+1,2):
    print(' ' * ((N-i)//2) + '*' * i)

