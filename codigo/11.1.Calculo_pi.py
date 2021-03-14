"""
Calculo de Pi
CC by SA @javacasm
3.14 14 de Marzo 2021

"""
import pygame
import random

width = 800
height = width
radio = width / 2

# 3 formas de definir los colores
red = pygame.Color('Red')
cyan = pygame.Color('cyan')
blue = pygame.Color(0,0,255) # ¿alpha?
green = (0,  255, 0)
white = (255,255,255)
black = (0,0,0)

pygame.init() # Inicializa el entorno de pygame

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Calculo de Pi')

running = True
screen.fill(black) # rellenamos la pantalla de verde
pygame.draw.circle(screen, white,(width/2,height/2),radio)

nPuntos = 0
nDentroCirculo = 0
radio2 = radio*radio
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    x = random.randint(0,width)
    y = random.randint(0,height)
    nPuntos += 1
    if (x-radio)*(x-radio) + (y-radio)*(y-radio) <= radio2: # Esta dentro del circulo
        screen.set_at((x,y),red)
        nDentroCirculo += 1
    else:
        screen.set_at((x,y),blue)

    pi = nDentroCirculo * 4 / nPuntos
    if nPuntos % 1000 == 0:
        print(nPuntos, pi)
    
    pygame.display.flip()  # actualizamos la pantalla

pygame.quit()     
