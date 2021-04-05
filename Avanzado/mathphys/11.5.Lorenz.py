'''
Lorenz's atractor
CC by SA @javacasm
April 2021
'''

from PIL import Image
import pygame
import time
import numpy as np
import math
import glob

width = 1200 # 1600//2
height = 1000 # //2
BLACK = (0, 0, 0)
LIGHTGREY = (100, 100, 100)
GREY = (160, 160, 160)
WHITE = (255,255,255)

num_steps = 10000

bSaveImages = True

theta = 0 # math.pi/4

def init():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Lorenz's atractor")

def calculateRotMatrix():
    global sintheta, costheta, theta
    sintheta = math.sin(theta)
    costheta = math.cos(theta)

def convert3DTo2D(x,y,z):
    # https://es.wikipedia.org/wiki/Matriz_de_rotaci%C3%B3n
    global sintheta, costheta, coordinatesAxes
    coordinatesAxes = None
    x2d = x * costheta - y * sintheta + width // 2
    y2d = x * sintheta + y * costheta - z + height * 3 // 4
    return [int(x2d),int(y2d)]

def convert3DTo2DIsometric(x,y,z):
    x2d = x-y + width//2
    y2d = (x + y )//2 - z + height//2
    return [x2d,y2d]

coordinatesAxes = None

def drawAxis():
    global screen,coordinatesAxes  

    if coordinatesAxes == None:
        centro = convert3DTo2D(0,0,0)
        ejeX = convert3DTo2D(500,0,0)
        ejeY = convert3DTo2D(0,500,0)
        ejeZ = convert3DTo2D(0,0,500)
        coordinatesAxes = [ejeX,centro,ejeY,centro,ejeZ,centro]

    pygame.draw.polygon(screen, WHITE, coordinatesAxes, 2)

  

def lorenzStep(x, y, z, s=10, r=28, b=2.667):
    """
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    """
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot



def createLorenz():
    global xs,ys,zs
    dt = 0.01

    # Need one more for the initial values
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    # Set initial values
    xs[0], ys[0], zs[0] = (0., 1., 1.05)

    # Step through "time", calculating the partial derivatives at the current point
    # and using them to estimate the next point

    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenzStep(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)

counter = 0
def drawLorenz():
    global xs,ys,zs, counter
    fx=15
    fy=fx
    fz = 5
    screen.fill(BLACK)
    drawAxis()
    for i in range(num_steps):
        iso = convert3DTo2D(int(xs[i]*fx),int(ys[i]*fy),int(zs[i]*fz))
        screen.set_at((iso[0],iso[1]),(0x10,0xf0,0xf0))
    pygame.display.flip()
    if bSaveImages:
        fichero = f'lorenz{counter:03d}.png'
        print(f'{fichero} saved')
        counter += 1
        pygame.image.save(screen,fichero)

def main():
    global theta, bSaveImages
    
    init()
    
    createLorenz()
   
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        calculateRotMatrix()
        drawLorenz()
        theta += 0.1
        if bSaveImages and theta >= math.pi * 2:
            frames = []
            imgs = glob.glob('lorenz*.png')
            imgs.sort()
            print(imgs)
            for i in imgs:
                new_frame = Image.open(i)
                frames.append(new_frame)

            # Save into a GIF file that loops forever
            frames[0].save('lorenz.gif', format='GIF',
                           append_images=frames[1:],
                           save_all=True,
                           duration=100, loop=1000)
            bSaveImages = False
            
    pygame.quit()

if __name__ == '__main__':
    main()
