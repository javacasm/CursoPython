'''
Dibujo del conjunto de Mandelbrot
CC by SA @javacasm
Marzo 2021
'''

import pygame
import time

width = 1600//2
height = 1200//2

def init():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Mandelbrot Set")


def main():

    init()
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
    pygame.quit()

if __name__ == '__main__':
    main()