"""
Calculo de Pi usando un cuarto de circulo y el cuadrado que lo contiene
CC by SA @javacasm
3.14 14 de Marzo 2021

"""

import random

width = 800
height = width
radio = width 


running = True

nPuntos = 0
nDentroCirculo = 0
radio2 = radio*radio

f = open('evo_pi.csv','wt')
f.write('N\tpi_value\n')

while running:
    x = random.randint(0,width)
    y = random.randint(0,height)
    nPuntos += 1
    if x*x + y*y <= radio2: # Esta dentro del circulo
        nDentroCirculo += 1

    if nPuntos % 10000 == 0:
        pi = nDentroCirculo * 4 / nPuntos
        sMsg =f'{nPuntos}\t{pi}\n'
        f.write(sMsg)
        if nPuntos % 1000000 == 0:
            print(sMsg,end='')
        
        
    
f.close()
