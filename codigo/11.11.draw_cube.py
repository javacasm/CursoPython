"""
This example shows a simple wireframe rotating cube.

Written by Gustavo Niemeyer <niemeyer@conectiva.com>.

Update by @javacasm

"""
from pygame.locals import *
import pygame.draw
import pygame.time
from math import sin, cos

ORIGINX = 0
ORIGINY = 0

def get2Dfrom3D(a):
    """Convert 3D coordinates to 2D""" 
    ax, ay = a[0]+(a[2]*0.3)+ORIGINX, a[1]+(a[2]*0.3)+ORIGINY
    return (ax,ay)

def draw_3dline(surface, color, a, b):
    """Draw line.""" 
    ax, ay = get2Dfrom3D(a)
    
    bx, by = get2Dfrom3D(b)
    
    pygame.draw.line(surface, color, (ax, ay), (bx, by))

def draw_cube_orig(surface, color, cube):
    """Draw 3D cube."""
    a, b, c, d, e, f, g, h = cube
    draw_3dline(surface, color, a, b)
    draw_3dline(surface, color, b, c)
    draw_3dline(surface, color, c, d)
    draw_3dline(surface, color, d, a)

    draw_3dline(surface, color, e, f)
    draw_3dline(surface, color, f, g)
    draw_3dline(surface, color, g, h)
    draw_3dline(surface, color, h, e)

    draw_3dline(surface, color, a, e)
    draw_3dline(surface, color, b, f)
    draw_3dline(surface, color, c, g)
    draw_3dline(surface, color, d, h)

def draw_cube_optimized(surface,color,cube):
    
    cube2d = []
    for point in cube:
        cube2d.append(get2Dfrom3D(point))

    pygame.draw.line(surface,color, cube2d[0],cube2d[1])
    pygame.draw.line(surface,color, cube2d[1],cube2d[2])
    pygame.draw.line(surface,color, cube2d[2],cube2d[3])
    pygame.draw.line(surface,color, cube2d[3],cube2d[0])
    
    pygame.draw.line(surface,color, cube2d[4],cube2d[5])
    pygame.draw.line(surface,color, cube2d[5],cube2d[6])
    pygame.draw.line(surface,color, cube2d[6],cube2d[7])
    pygame.draw.line(surface,color, cube2d[7],cube2d[4])

    pygame.draw.line(surface,color, cube2d[0],cube2d[4])
    pygame.draw.line(surface,color, cube2d[1],cube2d[5])
    pygame.draw.line(surface,color, cube2d[2],cube2d[6])
    pygame.draw.line(surface,color, cube2d[3],cube2d[7])


def rotate_3dpoint(p, angle, axis):
    """Rotate a 3D point around given axis."""
    ret = [0, 0, 0]
    cosang = cos(angle)
    sinang = sin(angle)
    ret[0] += (cosang+(1-cosang)*axis[0]*axis[0])*p[0]
    ret[0] += ((1-cosang)*axis[0]*axis[1]-axis[2]*sinang)*p[1]
    ret[0] += ((1-cosang)*axis[0]*axis[2]+axis[1]*sinang)*p[2]
    ret[1] += ((1-cosang)*axis[0]*axis[1]+axis[2]*sinang)*p[0]
    ret[1] += (cosang+(1-cosang)*axis[1]*axis[1])*p[1]
    ret[1] += ((1-cosang)*axis[1]*axis[2]-axis[0]*sinang)*p[2]
    ret[2] += ((1-cosang)*axis[0]*axis[2]-axis[1]*sinang)*p[0]
    ret[2] += ((1-cosang)*axis[1]*axis[2]+axis[0]*sinang)*p[1]
    ret[2] += (cosang+(1-cosang)*axis[2]*axis[2])*p[2]
    return ret

def rotate_object(obj, angle, axis):
    """Rotate an object around given axis."""
    for i in range(len(obj)):
        obj[i] = rotate_3dpoint(obj[i], angle, axis)

def main():
    global ORIGINX, ORIGINY
    pygame.init()
    screen = pygame.display.set_mode((320,200))
    # Move origin to center of screen
    ORIGINX = screen.get_width()//2
    ORIGINY = screen.get_height()//2
    cube = [(-50,50,50),  (50,50,50),  (50,-50,50),  (-50,-50,50),
            (-50,50,-50), (50,50,-50), (50,-50,-50), (-50,-50,-50)]
    theClock = pygame.time.Clock()
    average_clock = 0.0
    clock_count = 0
    N = 200
    while 1:
        event = pygame.event.poll()
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            break
        
        
        rotate_object(cube, 0.1, (0,1,0))
        rotate_object(cube, 0.01, (0,0,1))
        rotate_object(cube, 0.01, (1,0,0))

        screen.fill(0)
        draw_cube_optimized(screen, 255, cube)
        #draw_cube_orig(screen, 255, cube)
        pygame.display.flip()

        average_clock += theClock.get_fps()
        clock_count += 1
        if clock_count % N  == 0:
            print(f'{average_clock/N:2.0f}')
            average_clock = 0.0
            clock_count = 0
        theClock.tick()
    pygame.quit()

if __name__ == "__main__":
    main()