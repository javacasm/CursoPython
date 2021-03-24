# https://stackoverflow.com/questions/41332861/click-and-drag-a-rectangle-with-pygame

import pygame

# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = 430
SCREEN_HEIGHT = 410

#BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

FPS = 100

# --- classses --- (CamelCase names)

# empty

# --- functions --- (lower_case names)

# empty

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#screen_rect = screen.get_rect()

pygame.display.set_caption("Tracking System")

# - objects -



# - mainloop -

clock = pygame.time.Clock()

running = True

rectangle_draging = False
bDrawRect = False
rectangle = pygame.Rect(0,0,0,0)
while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rectangle_draging == False:
                    print('asignando posicion')
                    rectangle.x,rectangle.y = event.pos
                    rectangle_draging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                rectangle_draging = False
                print('UP')

        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                bDrawRect = True
                x1,y1 = event.pos
                rectangle.width = x1 - rectangle.x
                rectangle.height  = y1 - rectangle.y

    # - updates (without draws) -

    # empty

    # - draws (without updates) -

    screen.fill(WHITE)

    if bDrawRect:
        # print(rectangle)
        pygame.draw.rect(screen, RED, rectangle,width=1)

    pygame.display.flip()

    # - constant game speed / FPS -

    clock.tick(FPS)

# - end -

pygame.quit()
