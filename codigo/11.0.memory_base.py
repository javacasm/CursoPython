# from https://www.pygame.org/project/3675/5767
# Otra opción https://inventwithpython.com/pygame/chapter3.html
# https://stackoverflow.com/questions/59121989/blitting-images-onto-a-tile-that-is-part-of-a-grid-in-pygame
#Load modules and initialize display
import os, random, time, pygame

pygame.init()

#tamaño de la pantalla
SCREEN = (700,450)

#ICON = pygame.image.load(os.path.join("memory.png"))
#pygame.display.set_icon(ICON)

pygame.display.set_caption("Memory")
DISPLAY = pygame.display.set_mode(SCREEN)

# Colores

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fuentes de letras
ARIAL_200 = pygame.font.SysFont("Arial", 200)
ARIAL_50 = pygame.font.SysFont("Arial", 50)
ARIAL_35 = pygame.font.SysFont("Arial", 35)
ARIAL_20 = pygame.font.SysFont("Arial", 20)

ANCHO_CARTA = 100
MARGEN_CARTAS = 10
CARD_HOR_PAD = 37
CARD_VER_PAD = 22

nFilas = 4
nColumn = 5

# Creamos las cartas con los numeros del 0 al nFilas*nColumn/2
cards = [i for i in range(nFilas * nColumn // 2) for j in range(2)]
# Las desordenamos
random.shuffle(cards)

CARD_VAL_GRID = [cards[i*len(cards) // nFilas:(i+1)*len(cards) // nFilas] for i in range(nFilas)]

# Creamos una matriz de nFilas
CARD_GRID = [[] for i in range(nFilas)]

for i in range(nFilas):
    if i == 0:
        for j in range(nColumn):
            if j == 0:
                CARD_GRID[i].append(pygame.Rect(MARGEN_CARTAS, MARGEN_CARTAS, ANCHO_CARTA, ANCHO_CARTA))
            else:
                CARD_GRID[i].append(pygame.Rect(CARD_GRID[i][j-1].x + ANCHO_CARTA + MARGEN_CARTAS, MARGEN_CARTAS, ANCHO_CARTA, ANCHO_CARTA))
    else:
        for j in range(nColumn):
            if j == 0:
                CARD_GRID[i].append(pygame.Rect(MARGEN_CARTAS, CARD_GRID[i-1][0].y + ANCHO_CARTA + MARGEN_CARTAS, ANCHO_CARTA, ANCHO_CARTA))
            else:
                CARD_GRID[i].append(pygame.Rect(CARD_GRID[i][j-1].x + ANCHO_CARTA + MARGEN_CARTAS, CARD_GRID[i-1][0].y + ANCHO_CARTA + MARGEN_CARTAS, ANCHO_CARTA, ANCHO_CARTA))
global exposed
exposed = []
global matched
matched = []
global wrong
wrong = []
global intentos
intentos = 0

# bucle principal
while True:
    for event in pygame.event.get():
        # Terminamos
        if event.type == pygame.QUIT:
            pygame.quit()

    #Check for mouse click
    pressed = list(pygame.mouse.get_pressed())
    for i in range(len(pressed)):
        if pressed[i]:
            for i in range(nFilas):
                for j in range(nColumn):
                    mouse_pos = list(pygame.mouse.get_pos())
                    if mouse_pos[0] >= CARD_GRID[i][j].x and mouse_pos[1] >= CARD_GRID[i][j].y and mouse_pos[0] <= CARD_GRID[i][j].x + ANCHO_CARTA and mouse_pos[1] <= CARD_GRID[i][j].y + ANCHO_CARTA:
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
        intentos += 1
        if CARD_VAL_GRID[exposed[0][0]][exposed[0][1]] == CARD_VAL_GRID[exposed[1][0]][exposed[1][1]]:
            matched.extend(exposed)
            exposed.clear()
            
        else:
            wrong.extend(exposed)
            exposed.clear()

    #Clear screen
    DISPLAY.fill(BLACK)

    #Draw cards
    for i in range(nFilas):
        for j in range(nColumn):
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
    turn_text = ARIAL_20.render("intentos: " + str(intentos), True, WHITE)
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