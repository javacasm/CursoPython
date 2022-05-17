"""
Tutorial básico de pyGame
08.2 - Movimiento de formas con teclas:

Eventos de teclado:
Propiedades:
* key 
    pygame.K_q ...
    pygame.K_LEFT ...

Docs: 
* Eentos https://www.pygame.org/docs/ref/event.html
* Keys https://www.pygame.org/docs/ref/key.html

* Recursos en https://github.com/javacasm/CursoPython/blob/master/codigo/recursos_11.4.zip?raw=true

CC by SA @javacasm
Mayo 2022
"""

import pygame

width = 640
height = 400


# 3 formas de definir los colores
red = pygame.Color('Red')
cyan = pygame.Color('cyan')
blue = pygame.Color(0,0,255) # ¿alpha?
green = (0,  255, 0)
white = (255,255,255)
black = (0,0,0)

pygame.init() # Inicializa el entorno de pygame

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Movimiento rectángulo')

miImagen = pygame.image.load('./images/python-logo.png') # cargamos la imagen

# coordenadas del cuadrado
x = 200
y = 200

# velocidad de movimiento
vel = 1

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    if event.type == pygame.KEYDOWN:
            print('Tecla pulsada: '+event.unicode) # Para saber el código del carácter pulsado

            if event.key == pygame.K_q: # salimos con la tecla q
                running == False

            if event.key == pygame.K_LEFT:
                print('Movimiento izda')
                x -= vel

            if event.key == pygame.K_RIGHT:
                print('Movimiento drcha')                
                x += vel

            if event.key == pygame.K_UP:
                print('Movimiento arriba')
                y -= vel

            if  event.key == pygame.K_DOWN:
                print('Movimiento abajo')        
                y += vel

    screen.fill(black) # ponemos el fondo negro

    screen.blit(miImagen,(x, y)) # después copiamos la imagen

    pygame.display.flip()  # actualizamos la pantalla

pygame.quit()     