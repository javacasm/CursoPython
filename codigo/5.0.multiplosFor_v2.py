"""
 cálculo de multiplos de 5 y/o 7 entre 1 y 1000 usando bucle for

 License CC by SA
 by @javacasm

 8/3/2021

"""


for numero in range(1, 1001):
    bMultiplo5 = numero % 5 == 0  # comprobamos si es múltiplo de 5
    bMultiplo7 = numero % 7 == 0  # comprobamos si es múltiplo de 7
    strMensaje = ''
    if bMultiplo5 or bMultiplo7 :
        strMensaje = f' {numero} es múltiplo'
        if bMultiplo5 : 
            strMensaje += ' de 5'
        if bMultiplo7 :
            strMensaje += ' de 7'
        print(strMensaje)

