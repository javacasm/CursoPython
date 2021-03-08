"""
 Suma de los números hasta N

"""
N = int(input('¿Hasta que numero quieres que sume? '))

numero = 1
suma = 0
while numero <= N:
    suma += numero
    numero += 1

print(f'La suma de los números hasta {N} es {suma}')

print('Sabiendo algo de álgebra: ', (1+N)*N//2)
