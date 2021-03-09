# Sumas de enteros has N
N = int(input('¿Numero? '))

suma = 0
sumando = 1
while sumando <= N:
    suma += sumando
    sumando += 1

print(f'La suma hasta {N} es: {suma}')
print(f'Algebraicamente es {N*(N+1)//2}')