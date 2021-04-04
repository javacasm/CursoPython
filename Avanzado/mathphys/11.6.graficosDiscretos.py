'''
Dibujo del conjunto de Mandelbrot
CC by SA @javacasm
Marzo 2021
'''

import pygame
import time

width = 1600
height = 1200

def init():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Mandelbrot Set")

def drawMod(k):
    for x in range(width):
        for y in range(height):
            i = (1 == (abs(x+y)^abs(x-y)+1) % k) * 255
            screen.set_at((x,y),(i,i,i))

    pygame.display.flip()   

def main():
    global screen
    init()


    running = True
    k = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        print(f'k = {k}')
        drawMod(k)
        
        k += 1
    pygame.quit()

if __name__ == '__main__':
    main()
