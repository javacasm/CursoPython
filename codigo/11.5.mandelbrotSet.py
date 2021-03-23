import pygame
import sys

SCREENWIDTH = 800
SCREENHEIGHT = 600
max_iteration = 20

pygame.init()

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT),pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Mandelbrot Fractal")

fractal = screen.copy()


fractal.fill((0,0,0))
for i in range(SCREENWIDTH):
    for j in range(SCREENHEIGHT):
        x0 = (float(i)/SCREENWIDTH)*3.5 - 2.1
        y0 = (float(j)/SCREENHEIGHT)*2.4 - 1.2

        x = 0
        y = 0

        iteration = 0

        while x*x + y*y < 4 and iteration < max_iteration:
            xtemp = x*x - y*y + x0
            y = 2*x*y + y0

            x = xtemp

            iteration = iteration + 1
        
        color = iteration *10
        fractal.set_at((i,j), (color,color,color))

    # print(f'{i}')
    if i%20 == 0:
        screen.blit(fractal, (0,0))
        pygame.display.flip()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            