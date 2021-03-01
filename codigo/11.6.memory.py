"""
Recursos

Musica

https://freemusicarchive.org/music/sawsquarenoise/dojokratos/stage-3
Stage 3 by sawsquarenoise  https://creativecommons.org/licenses/by/4.0/
 
Sonidos de https://mixkit.co/free-sound-effects/game/

# Otra opción https://inventwithpython.com/pygame/chapter3.html
# https://stackoverflow.com/questions/59121989/blitting-images-onto-a-tile-that-is-part-of-a-grid-in-pygame


"""
import random, pygame

pygame.init()

nFilas = 4
nColumn = 4

ANCHO_CARTA = 110
MARGEN_ENTRE_CARTAS = 10

screen_size = ((ANCHO_CARTA + MARGEN_ENTRE_CARTAS) * nColumn
, (ANCHO_CARTA + MARGEN_ENTRE_CARTAS) * nFilas)

# Colores

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuentes de letras
ARIAL_200 = pygame.font.SysFont("Arial", ANCHO_CARTA)

imageFiles = ['images/bola.png', 'images/bumeran.png', 'images/coche.png', 'images/cohete.png', 'images/manzana.png', 'images/pez.png', 'images/polo.png','images/banana.png']

images = []

for imageFile in imageFiles:
    imagen = pygame.image.load(imageFile)
    images.append(imagen)
print(f'Hay {len(images)}')

imagenOculto = pygame.image.load('images/interrogacion.png')

pygame.display.set_caption('Memory')

display = pygame.display.set_mode(screen_size)

class Carta():
    def __init__(self,x,y,text,idImagen):
        self.x = x
        self.y = y
        self.text = text
        self.isVisible = False
        self.myRect = (self.x,self.y,ANCHO_CARTA,ANCHO_CARTA)
        self.idImagen = idImagen
        self.isVolteado = False

    def getText(self):
        return self.text

    def isInside(self,x,y):
        if self.x < x < self.x + ANCHO_CARTA:
            if self.y < y < self.y + ANCHO_CARTA:
                return True
            
        return False

    def volteado(self, volteo):
        self.isVolteado = volteo

    def isVisible(self):
        return self.isVisible
    
    def setVisible(self):
        self.isVisible = not self.isVisible

    def draw(self,screen):
        # pygame.draw.rect(Tile.surface, Tile.fg_color, self.rect, Tile.border_width) 
        #         image_rect = self.content.get_rect(center = self.rect.center)
        # Tile.surface.blit(self.content, image_rect)
        if self.isVisible or self.isVolteado:
            screen.blit(images[self.idImagen],(self.x, self.y)) # después copiamos la imagen
            # dib = ARIAL_200.render(self.text,True,WHITE)
            # screen.blit(dib, (self.x + MARGEN_ENTRE_CARTAS, self.y + MARGEN_ENTRE_CARTAS))
        else:
            screen.blit(imagenOculto,(self.x, self.y)) # después copiamos la imagen
            # pygame.draw.rect(screen,WHITE,self.myRect)

cartas = []

idDibujos = [e for e in range(0,nFilas*nColumn // 2)] * 2

random.shuffle(idDibujos)

contador = 0
for i in range(0,nColumn):
    for j in range(0,nFilas):
        xPos = (ANCHO_CARTA + MARGEN_ENTRE_CARTAS) * i
        yPos = (ANCHO_CARTA + MARGEN_ENTRE_CARTAS) * j
        carta = Carta(xPos, yPos, str(idDibujos[contador]),idDibujos[contador])
        cartas.append(carta)
        contador += 1

bRunning = True
bHayCambios = True
while bRunning:

    for event in pygame.event.get():
        # Terminamos
        if event.type == pygame.QUIT:
            pygame.quit()
    
    if pygame.mouse.get_pressed()[0]:
        (mouse_x,mouse_y) = pygame.mouse.get_pos()
        print((mouse_x,mouse_y))
        for carta in  cartas:
            if carta.isInside(mouse_x,mouse_y):
                carta.volteado(True)
                bHayCambios = True

    if bHayCambios:
        display.fill(BLACK)
        for carta in cartas:
            carta.draw(display)
        bHayCambios = False

    pygame.display.flip()


