# Escribe tu código aquí :-)

multiplos5 = []
multiplos7 = []
multiplos5y7 = []

for numero in range(1, 1001):
    bMultiplo5 = numero % 5 == 0
    bMultiplo7 = numero % 7 == 0
    if bMultiplo5 and bMultiplo7 :
        print(numero , ' es múltiplo de 5 y de 7')
        multiplos5.append(numero)
        multiplos7.append(numero)
        multiplos5y7.append(numero)
    elif bMultiplo5 :
        print(numero , ' es múltiplo de 5')
        multiplos5.append(numero)
    elif bMultiplo7 :
        print(numero , ' es múltiplo de 5 y de 7')
        multiplos7.append(numero)


print('Múltiplos de 5: ', multiplos5)
print('Múltiplos de 7 ', multiplos7)
print('Múltiplos de 5 y 7', multiplos5y7)
