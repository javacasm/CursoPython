'''
Dibujo del conjunto de Mandelbrot
CC by SA @javacasm
Marzo 2021
'''

import pygame
import time

width = 1600//2
height = 1200//2
max_iteracion = 220
factor_color = 220 // max_iteracion

ROJO   = (255,   0,   0)

x0Min = -2.1
y0Min = -1.2
x0Max =  0.8
y0Max =  1.2


def calculateFactors():
    global fx0, fy0, x0Min, y0Min, x0Max, y0Max 
    dx0 = x0Max - x0Min
    dy0 = y0Max - y0Min

    fx0 = dx0/width
    fy0 = dy0/height

    
def iteraMandelbrot(x0,y0):
    x, y = 0, 0
    iteracion = 0
    while iteracion < max_iteracion and x*x + y*y < 4 :
        xnew = x*x - y*y + x0
        y = 2*x*y + y0

        x = xnew
        iteracion += 1
       
    return iteracion


def init():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Mandelbrot Set")

def drawMandelbrot(i0=0,j0=0,stepI=1,stepJ=1,clear = False):
    global screen,fx0,fy0,x0Min,y0Min
    if clear:
        screen.fill((0,0,0))

    for i in range(i0,width,stepI):
        for j in range(j0,height,stepJ):
            x0 = i*fx0 + x0Min
            y0 = j*fy0 + y0Min

            iteracion = iteraMandelbrot(x0,y0)
           
            color = iteracion * factor_color
            screen.set_at((i,j), (color,color,color))

        pygame.display.flip()

def repintaZona():
    global fractal
    calculateFactors()
    drawMandelbrot(clear = True)
    fractal = screen.copy() 

def refrescaPantalla():
    screen.blit(fractal, (0,0))
    pygame.display.flip()

def main():

    init()
    repintaZona()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
    pygame.quit()

if __name__ == '__main__':
    main()