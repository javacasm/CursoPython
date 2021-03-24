# https://stackoverflow.com/questions/64716266/how-can-i-make-a-rectangle-selection-tool-in-python-3
import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
rect1 = pg.Rect(100, 100, 161, 100)
rect2 = pg.Rect(300, 200, 161, 100)
selected_rect = None

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            for rect in (rect1, rect2):
                if rect.collidepoint(event.pos):
                    selected_rect = rect  # Select the colliding rect.
        elif event.type == pg.MOUSEBUTTONUP:
            selected_rect = None  # De-select the rect.
        elif event.type == pg.MOUSEMOTION:
            if selected_rect is not None:  # If a rect is selected.
                if event.buttons[0]:  # Left mouse button is down.
                    # Move the rect.
                    selected_rect.x += event.rel[0]
                    selected_rect.y += event.rel[1]
                else:  # Right or middle mouse button.
                    # Scale the rect.
                    selected_rect.w += event.rel[0]
                    selected_rect.h += event.rel[1]
                    selected_rect.w = max(selected_rect.w, 10)
                    selected_rect.h = max(selected_rect.h, 10)

    screen.fill((30, 30, 30))
    pg.draw.rect(screen, (0, 100, 250), rect1)
    pg.draw.rect(screen, (0, 200, 120), rect2)
    pg.display.flip()
    clock.tick(30)