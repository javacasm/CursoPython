# Tarea 3
"""
 cálculo de multiplos de 5 y/o 7 entre 1 y 1000 usando bucle for

 License CC by SA
 by @javacasm

 6/4/2020

"""

multiplos5 = []
multiplos7 = []
multiplos5y7 = []
multiplos5o7 = []

for numero in range(1, 1001):
    bMultiplo5 = numero % 5 == 0  # comprobamos si es múltiplo de 5
    bMultiplo7 = numero % 7 == 0  # comprobamos si es múltiplo de 7
    if bMultiplo5 and bMultiplo7 :
        print(numero , ' es múltiplo de 5 y de 7')
        multiplos5.append(numero)
        multiplos7.append(numero)
        multiplos5y7.append(numero)
        multiplos5o7.append(numero)
    elif bMultiplo5 :
        print(numero , ' es múltiplo de 5')
        multiplos5.append(numero)
        multiplos5o7.append(numero)
    elif bMultiplo7 :
        print(numero , ' es múltiplo de 5 y de 7')
        multiplos7.append(numero)
        multiplos5o7.append(numero)


print('Múltiplos de 5: ', multiplos5)
print('Múltiplos de 7 ', multiplos7)
print('Múltiplos de 5 y 7', multiplos5y7)
print('Múltiplos de 5 o 7', multiplos5o7)
