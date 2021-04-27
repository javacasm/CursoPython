'''
Lorenz's atractor
CC by SA @javacasm
April 2021
'''

v = '2.1'

from PIL import Image
import pygame
# import time
import numpy as np
import math
import glob
import random

width = 1200 # 1600//2
height = 1000 # //2

# Colors
BLACK = (0, 0, 0)
LIGHTGREY = (100, 100, 100)
GREY = (160, 160, 160)
WHITE = (255,255,255)
RED = (200,50,50)
GREEN = (50,200,50)
BLUE = (50,50,200)
colorBack = (0x70,0x70,0x70)
colorFore = (0x10,0xf0,0xf0)

# points number 
N_Puntos = 2
Max_Puntos = 20000

num_back_dots = 5000

t = 0 # time
bSaveImages = False

## math cache

theta = 0 # math.pi/4
sintheta = 0.0
costheta = 0.0

# Puntos que evolucionan
xs = []
ys = []
zs = []

# Puntos del atractor como referencia

xs_b = np.empty(num_back_dots + 1)
ys_b = np.empty(num_back_dots + 1)
zs_b = np.empty(num_back_dots + 1)

# integracion

dt = 0.02

# graphics

screen = None
font = None

animCounter = 0  # Contador para animacion

# graphic cache

imgX = imgY = imgZ = None

coordinatesAxes = None

# Lorenz constants

s0 = 10
r0 = 28
b0 = 2.667
puntoInicial = (xs_0, ys_0, zs_0) = (0., 1., 1.05)
length = 0

def init():
    global screen, font, imgX, imgY, imgZ
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Lorenz's atractor")
    sysfont = pygame.font.get_default_font()
    print(f'font: {sysfont}')
    font = pygame.font.SysFont(None, 48)
    imgX = font.render('X' , True, RED)
    imgY = font.render('Y' , True, GREEN)
    imgZ = font.render('Z' , True, BLUE)    

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

def lorenzStep(x, y, z, s = s0, r = r0, b = b0):
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


def createLorenzFondo():
    global xs_b, ys_b, zs_b, dt

    xs_b[0], ys_b[0], zs_b[0] = puntoInicial

    for i in range(num_back_dots):
        x_dot, y_dot, z_dot = lorenzStep(xs_b[i], ys_b[i], zs_b[i])
        xs_b[i + 1] = xs_b[i] + (x_dot * dt)
        ys_b[i + 1] = ys_b[i] + (y_dot * dt)
        zs_b[i + 1] = zs_b[i] + (z_dot * dt)

def createLorenz():
    global xs, ys, zs, N_Puntos, xs_0, ys_0, zs_0

    # Puntos iniciales
    for _ in range(N_Puntos):
        xs.append(xs_0 + random.uniform(-0.01,0.01))
        ys.append(ys_0 + random.uniform(-0.1,0.1))
        zs.append(zs_0 + random.uniform(-0.1,0.1))

def nextLorenzStep():
    global xs, ys, zs, N_Puntos, Max_Puntos, t    

    t += dt

    for i in range(N_Puntos):
        x_dot, y_dot, z_dot = lorenzStep(xs[i], ys[i], zs[i])
        xs[i] += x_dot * dt
        ys[i] += y_dot * dt
        zs[i] += z_dot * dt
    if N_Puntos<Max_Puntos:
        addIntermediatePoints()
        
def addIntermediatePoints():
    global xs, ys, zs, N_Puntos, length
    nInicial = N_Puntos
    xs_old = xs
    xs = []
    ys_old = ys
    ys = []
    zs_old = zs
    zs = []
    x_old = xs_old[0]
    y_old = ys_old[0]
    z_old = zs_old[0]
    N_Puntos = 0
    length = 0
    for i in range(nInicial):
        x = xs_old[i]
        y = ys_old[i]
        z = zs_old[i]
        mod = math.sqrt((x_old - x)**2 + (y_old - y)**2 + (z_old - z)**2 )
        if mod > 10:
            xs.append((x_old + x)/2)
            ys.append((y_old + y)/2)
            zs.append((z_old + z)/2)
            N_Puntos += 1
        length += mod
        xs.append(x)
        ys.append(y)
        zs.append(z)
        N_Puntos += 1
        x_old = x
        y_old = y
        z_old = z
      
            
    if nInicial != N_Puntos:
        print(f'Añadidos {N_Puntos-nInicial} a {nInicial}')
        
def drawAxis():
    global screen,coordinatesAxes
    global imgX, imgY, imgZ

    if coordinatesAxes == None:
        centro = convert3DTo2D(0,0,0)
        ejeX = convert3DTo2D(500,0,0)
        ejeY = convert3DTo2D(0,500,0)
        ejeZ = convert3DTo2D(0,0,500)
        coordinatesAxes = [ejeX,centro,ejeY,centro,ejeZ,centro]

    pygame.draw.polygon(screen, GREY, coordinatesAxes, 1)

    screen.blit(imgX, ejeX)
    screen.blit(imgY, ejeY)
    screen.blit(imgZ, ejeZ)
    
def drawLorenz():
    global xs,ys,zs,xs_b,ys_b,zs_b, animCounter, N_Puntos, font, t, lentgh
    fx = 15
    fy = fx
    fz = 5
    screen.fill(BLACK)
    drawAxis()
    for i in range(N_Puntos):
        iso = convert3DTo2D(int(xs[i]*fx),int(ys[i]*fy),int(zs[i]*fz))
        screen.set_at(iso,colorFore)
        
    for i in range(num_back_dots):
        iso = convert3DTo2D(int(xs_b[i]*fx),int(ys_b[i]*fy),int(zs_b[i]*fz))
        screen.set_at(iso,colorBack)

    img = font.render(f'N:{N_Puntos} t = {t:5.2f} length = {length:10.2f}' , True, WHITE)
    screen.blit(img, (20, 20))
    pygame.display.flip()
    if bSaveImages:
        fichero = f'lorenz{animCounter:03d}.png'
        print(f'{fichero} saved')
        animCounter += 1
        pygame.image.save(screen,fichero)

def main():
    global theta, bSaveImages
    
    print(f'v:{v}')
    
    init()
    createLorenzFondo()
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
                elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False
        calculateRotMatrix()
        nextLorenzStep()
        drawLorenz()
        theta += 0.01
 
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
