import pygame
import numpy as np

width = 1200 #//2
height = 800 #//2
max_iteracion = 20
factorColor = 255//max_iteracion
dw = dh = 20

def iteraMandelbrot(x0,y0):
    global max_iteracion
    x = 0
    y = 0

    iteracion = 0

    while x*x + y*y < 4 and iteracion < max_iteracion:
        xtemp = x*x - y*y + x0
        y = 2*x*y + y0

        x = xtemp

        iteracion += 1
    return iteracion

def getX0Y0(i,j):
    x0 = (float(i)/width)*3.5 - 2.1
    y0 = (float(j)/height)*2.4 - 1.2  
    return x0,y0

def getMandel(i,j):
    global mandel
    if mandel[i,j] == 0:
        x0, y0 = getX0Y0(i,j)
        iteracion = iteraMandelbrot(x0,y0)
        mandel[i,j] = iteracion
    else:
        iteracion = mandel[i,j]

    return iteracion

def addRect(x,y,dx,dy):
    global pendientes
    if not (x,y,dx,dy) in pendientes:
        pendientes.append((x,y,dx,dy))

def drawSquare(i,j,dx,dy):
    global fractal, factorColor
    if dx >= 2 and dy >= 2:
        iteracion00   = getMandel(i,   j)
        iteraciondx0  = getMandel(i+dx,j)
        iteracion0dy  = getMandel(i,   j+dy)
        iteraciondxdy = getMandel(i+dx,j+dy)
        
        if iteracion00 == iteraciondxdy and  iteracion00 == iteracion0dy and  iteracion00 == iteraciondx0 and dx <20:
            color = iteracion00 * factorColor
            if dx>50:
                print(f'{iteracion00} {dx} {dy} ')
        else:
            dx2 = dx//2
            dy2 = dy//2
            if dx2>0 and dy2>0:
                if iteracion00 != iteraciondx0:
                    addRect(i,     j,     dx2,dy2)
                    addRect(i+dx2, j,     dx2,dy2)
                if iteraciondx0 != iteraciondxdy:
                    addRect(i+dx2, j,     dx2,dy2)
                    addRect(i+dx2, j+dy2, dx2,dy2)
                if iteracion00 != iteracion0dy:
                    addRect(i,     j,     dx2,dy2)
                    addRect(i,     j+dy2, dx2,dy2)
                if iteracion0dy != iteraciondxdy:
                    addRect(i,     j+dy2, dx2,dy2)
                    addRect(i+dx2, j+dy2, dx2,dy2)
            else:
                print(f'{dx2} {dy2}')
            color = (iteracion00 + iteraciondxdy + iteracion0dy + iteraciondx0) * factorColor // 4
    else:
        iteracion = getMandel(i,j)
        color =iteracion * factorColor  
    pygame.draw.rect(fractal,(color,color,color),(i,j,dx+1,dy+1))
  

pygame.init()

screen = pygame.display.set_mode((width,height),pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Mandelbrot Fractal")

fractal = screen.copy()


fractal.fill((0,0,0))

mandel = np.zeros((width + dw, height + dh))

pendientes = []
pendientesOld = []

for i in range(0,width,dw):
    for j in range(0,height,dh):
        drawSquare(i,j,dw,dh)

screen.blit(fractal, (0,0))
pygame.display.flip()

contador = 0
while len(pendientes) > 0:
    
    pendientesOld = pendientes
    pendientes = []
    # print(f'pendientes {len(pendientesOld)}')
    while len(pendientesOld)>0:
         x,y,dx,dy = pendientesOld.pop()
     
         contador += 1
         drawSquare(x,y,dx,dy)
         if contador%100 == 0:
             screen.blit(fractal, (0,0))
             pygame.display.flip()
             print(f'pendientes: {len(pendientesOld)}')
             
print(f'hemos terminado {len(pendientes)} {len(pendientesOld)}')
screen.blit(fractal, (0,0))
pygame.display.flip()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()