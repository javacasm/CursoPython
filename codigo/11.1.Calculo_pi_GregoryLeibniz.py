'''
http://edupython.blogspot.com/2015/03/pensando-en-pi.html

serie de Gregory–Leibniz
 
π = 4(1 - 1/3 + 1/5 - 1/7 + ...)

'''

import time

def getSerieGregoryLeibniz(n):
    suma = 0
    for k in range(1,n+1):
        suma += (-1)**(k+1)/(2*k-1)
    
    resultado = 4 * suma
    return resultado

def muestraResultado(str):
    print(str)
    f = open('tiempos_python.csv','at')
    f.write(str + "\n")
    f.close()

for n in range(1,12):
    inicio = time.time()
    valor = getSerieGregoryLeibniz(10**n)
    str = '{2:.2f} {1} {0:.{1}f}'.format(valor,n,time.time()-inicio)
    muestraResultado(str)
