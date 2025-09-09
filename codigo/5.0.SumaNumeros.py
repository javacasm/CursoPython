# Sumas de enteros has N
N = int(input('¿Numero? '))

suma = 0
for sumando in range(1,N+1):
    suma += sumando

print(f'La suma hasta {N} es: {suma}')
print(f'Algebraicamente es {N*(N+1)//2}')
