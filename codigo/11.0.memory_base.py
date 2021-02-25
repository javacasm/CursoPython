# from https://www.pygame.org/project/3675/5767
# Otra opción https://inventwithpython.com/pygame/chapter3.html
# https://stackoverflow.com/questions/59121989/blitting-images-onto-a-tile-that-is-part-of-a-grid-in-pygame
#Load modules and initialize display
import os, random, time, pygame
pygame.init()
SCREEN = (700,450)
#ICON = pygame.image.load(os.path.join("memory.png"))
#pygame.display.set_icon(ICON)
pygame.display.set_caption("Memory")
DISPLAY = pygame.display.set_mode(SCREEN)

#Define objects and generate number grid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ARIAL_200 = pygame.font.SysFont("Arial", 200)
ARIAL_50 = pygame.font.SysFont("Arial", 50)
ARIAL_35 = pygame.font.SysFont("Arial", 35)
ARIAL_20 = pygame.font.SysFont("Arial", 20)
CARD_LEN = 100
CARD_MARGIN = 10
CARD_HOR_PAD = 37
CARD_VER_PAD = 22
ROWS = 4
COLS = 5
cards = [i for i in range(10) for j in range(2)]
random.shuffle(cards)
CARD_VAL_GRID = [cards[i*len(cards) // ROWS:(i+1)*len(cards) // ROWS] for i in range(ROWS)]
CARD_GRID = [[] for i in range(ROWS)]
for i in range(ROWS):
    if i == 0:
        for j in range(COLS):
            if j == 0:
                CARD_GRID[i].append(pygame.Rect(CARD_MARGIN, CARD_MARGIN, CARD_LEN, CARD_LEN))
            else:
                CARD_GRID[i].append(pygame.Rect(CARD_GRID[i][j-1].x + CARD_LEN + CARD_MARGIN, CARD_MARGIN, CARD_LEN, CARD_LEN))
    else:
        for j in range(COLS):
            if j == 0:
                CARD_GRID[i].append(pygame.Rect(CARD_MARGIN, CARD_GRID[i-1][0].y + CARD_LEN + CARD_MARGIN, CARD_LEN, CARD_LEN))
            else:
                CARD_GRID[i].append(pygame.Rect(CARD_GRID[i][j-1].x + CARD_LEN + CARD_MARGIN, CARD_GRID[i-1][0].y + CARD_LEN + CARD_MARGIN, CARD_LEN, CARD_LEN))
global exposed
exposed = []
global matched
matched = []
global wrong
wrong = []
global turns
turns = 0

#Game loop
while True:
    for event in pygame.event.get():
        #Detect quit
        if event.type == pygame.QUIT:
            pygame.quit()

    #Check for mouse click
    pressed = list(pygame.mouse.get_pressed())
    for i in range(len(pressed)):
        if pressed[i]:
            for i in range(ROWS):
                for j in range(COLS):
                    mouse_pos = list(pygame.mouse.get_pos())
                    if mouse_pos[0] >= CARD_GRID[i][j].x and mouse_pos[1] >= CARD_GRID[i][j].y and mouse_pos[0] <= CARD_GRID[i][j].x + CARD_LEN and mouse_pos[1] <= CARD_GRID[i][j].y + CARD_LEN:
                        global has_instance
                        has_instance = False
                        for k in range(len(exposed)):
                            if exposed[k] == [i, j]:
                                has_instance = True

                        for k in range(len(matched)):
                            if matched[k] == [i, j]:
                                has_instance = True

                        if has_instance == False:
                            exposed.append([i, j])
                            
    if len(exposed) == 2:
        turns += 1
        if CARD_VAL_GRID[exposed[0][0]][exposed[0][1]] == CARD_VAL_GRID[exposed[1][0]][exposed[1][1]]:
            matched.extend(exposed)
            exposed.clear()
            
        else:
            wrong.extend(exposed)
            exposed.clear()

    #Clear screen
    DISPLAY.fill(BLACK)

    #Draw cards
    for i in range(ROWS):
        for j in range(COLS):
            pygame.draw.rect(DISPLAY, (255, 255, 255), CARD_GRID[i][j])
            
    #Draw numbers
    if exposed:
        for i in exposed:
            text = str(CARD_VAL_GRID[i[0]][i[1]])
            render = ARIAL_50.render(text, True, BLACK)
            DISPLAY.blit(render, (CARD_GRID[i[0]][i[1]].x + CARD_HOR_PAD, CARD_GRID[i[0]][i[1]].y + CARD_VER_PAD))

    if matched:
        for i in matched:
            text = str(CARD_VAL_GRID[i[0]][i[1]])
            render = ARIAL_50.render(text, True, GREEN)
            DISPLAY.blit(render, (CARD_GRID[i[0]][i[1]].x + CARD_HOR_PAD, CARD_GRID[i[0]][i[1]].y + CARD_VER_PAD))

    if wrong:
        for i in wrong:
            text = str(CARD_VAL_GRID[i[0]][i[1]])
            render = ARIAL_50.render(text, True, RED)
            DISPLAY.blit(render, (CARD_GRID[i[0]][i[1]].x + CARD_HOR_PAD, CARD_GRID[i[0]][i[1]].y + CARD_VER_PAD))

    #Draw other stuff
    title = ARIAL_35.render("Memory", True, WHITE)
    DISPLAY.blit(title, (570, 10))
    turn_text = ARIAL_20.render("Intentos: " + str(turns), True, WHITE)
    DISPLAY.blit(turn_text, (580, 75))

    #Check win
    if len(matched) == 20:
        DISPLAY.fill(BLACK)
        win = ARIAL_200.render("¡Ganaste!", True, GREEN)
        DISPLAY.blit(win, (40, 105))
        pygame.display.flip()
        break
    
    pygame.display.flip()
    if wrong:
        time.sleep(1)
        wrong.clear()