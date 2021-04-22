'''
Lorenz's atractor
CC by SA @javacasm
April 2021
'''

v = '1.1'

from PIL import Image
import pygame
import time
# import numpy as np
import math
import glob
import random

width = 1200 # 1600//2
height = 1000 # //2
BLACK = (0, 0, 0)
LIGHTGREY = (100, 100, 100)
GREY = (160, 160, 160)
WHITE = (255,255,255)

N_Puntos = 2
Max_Puntos = 25000
t = 0
bSaveImages = False

theta = 0 # math.pi/4

def init():
    global screen, font
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Lorenz's atractor")
    sysfont = pygame.font.get_default_font()
    print(f'font: {sysfont}')
    font = pygame.font.SysFont(None, 48)    

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
    global xs, ys, zs, N_Puntos

    xs = []
    ys = []
    zs = []

    # Puntos iniciales


    xs_0, ys_0, zs_0 = (0., 1., 1.05)
    for i in range(N_Puntos):
        xs.append(xs_0 + random.uniform(-0.01,0.01))
        ys.append(ys_0 + random.uniform(-0.1,0.1))
        zs.append(zs_0 + random.uniform(-0.1,0.1))

def nextLorenzStep():
    global xs, ys, zs, N_Puntos, Max_Puntos, t    
    dt = 0.01
    t += dt
    nInicial = N_Puntos
    for i in range(N_Puntos):
        x_dot, y_dot, z_dot = lorenzStep(xs[i], ys[i], zs[i])
        xs[i] += x_dot * dt
        ys[i] += y_dot * dt
        zs[i] += z_dot * dt
        
        dv = x_dot*x_dot + y_dot*y_dot + z_dot*z_dot
        v = xs[i]*xs[i] + ys[i]*ys[i] + zs[i]*zs[i]
        if dv/v > 105 and N_Puntos < Max_Puntos:
            #print(dv/v)
            xs.append(xs[i] - x_dot * dt / 2)
            ys.append(ys[i] - y_dot * dt / 2)
            zs.append(zs[i] - z_dot * dt / 2)
            N_Puntos += 1
    if nInicial != N_Puntos:
        print(f'Añadidos {N_Puntos-nInicial} a {nInicial}')
counter = 0

def drawLorenz():
    global xs,ys,zs, counter, N_Puntos, font, t
    fx = 15
    fy = fx
    fz = 5
    screen.fill(BLACK)
    drawAxis()
    for i in range(N_Puntos):
        iso = convert3DTo2D(int(xs[i]*fx),int(ys[i]*fy),int(zs[i]*fz))
        screen.set_at((iso[0],iso[1]),(0x10,0xf0,0xf0))
    
    img = font.render(str(N_Puntos) + ' t = '+str(t) , True, WHITE)
    screen.blit(img, (20, 20))
    pygame.display.flip()
    if bSaveImages:
        fichero = f'lorenz{counter:03d}.png'
        print(f'{fichero} saved')
        counter += 1
        pygame.image.save(screen,fichero)

def main():
    global theta, bSaveImages
    
    print(f'v:{v}')
    
    init()
    
    createLorenz()
   
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    bSaveImages = True
                    theta = 0
        calculateRotMatrix()
        nextLorenzStep()
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
