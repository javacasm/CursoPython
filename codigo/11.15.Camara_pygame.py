import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

camlist = pygame.camera.list_cameras()
if camlist != None:
    print(f'Hay {len(camlist)}')
    for cam in camlist:
        print(cam)
    size = (640,480)
    cam = pygame.camera.Camera(camlist[2],size)
    cam.start()
    image = cam.get_image()
    cam.set_controls(hflip = True, vflip = False)
    print(cam.get_controls())
    display = pygame.display.set_mode(size, 0)
    snapshot = pygame.surface.Surface(size, 0, display)
    going = True
    while going:
        events = pygame.event.get()
        for e in events:
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                # close the camera safely
                cam.stop()
                going = False
        if cam.query_image():
            snapshot = cam.get_image(snapshot)
        display.blit(snapshot, (0,0))
        pygame.display.flip()
        
