"""
 Suma de los números hasta N


 License CC by SA
 by @javacasm

 9/4/2020


"""
N = 100000000

numero = 1
suma = 0
while numero <= N:
    suma += numero
    numero += 1

print('La suma de los números hasta %d es ' % N, suma)

print('Sabiendo algo de álgebra: ', (1+N)*N//2)
