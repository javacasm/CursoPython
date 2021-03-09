"""
 cálculo de multiplos de 5 y/o 7 entre 1 y 1000 usando bucle for

 License CC by SA
 by @javacasm

 8/3/2021

"""


for numero in range(1, 1001):
    bMultiplo5 = numero % 5 == 0  # comprobamos si es múltiplo de 5
    bMultiplo7 = numero % 7 == 0  # comprobamos si es múltiplo de 7
    if bMultiplo5 and bMultiplo7 :
        print(f' {numero} es múltiplo de 5 y de 7')
    elif bMultiplo5 :
        print(f' {numero} es múltiplo de 5')
    elif bMultiplo7 :
        print(f' {numero} es múltiplo de 5 y de 7')

