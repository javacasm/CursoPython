"""
Recursos

Musica - free youtube library
Sonidos de https://mixkit.co/free-sound-effects/game/

Imagenes de https://stackoverflow.com/questions/59121989/blitting-images-onto-a-tile-that-is-part-of-a-grid-in-pygame

"""
import random, pygame, time, sys
v = '0.9'

nFilas = 4
nColumn = 4

ANCHO_CARTA = 110
MARGEN_ENTRE_CARTAS = 10
ALTO_TEXTO = 100

screen_size = ((ANCHO_CARTA + MARGEN_ENTRE_CARTAS) * nColumn, 
             (ANCHO_CARTA + MARGEN_ENTRE_CARTAS) * nFilas + ALTO_TEXTO)

# Colores

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicializamos pyGame
pygame.init()

# Fuentes de letras
ARIAL_100 = pygame.font.SysFont("Arial", ANCHO_CARTA)

# Inicializamos el sonido
pygame.mixer.init()
volteoSound = pygame.mixer.Sound('music/Volteo.wav')

pygame.mixer.music.load('./music/Fortunate Note - Silent Partner.ogg') 
pygame.mixer.music.set_volume(0.5 ) # volumen entre 0 y 1.0
pygame.mixer.music.play()

# Nombre de las imagenes que usaremos
imageFiles = ['images/bola.png', 'images/bumeran.png', 'images/coche.png',
              'images/cohete.png', 'images/manzana.png', 'images/pez.png',
              'images/polo.png','images/banana.png']

images = [] # guardaremos los pygame.image para usarlos
for imageFile in imageFiles:
    imagen = pygame.image.load(imageFile)
    images.append(imagen)

imagenOculto = pygame.image.load('images/interrogacion.png')

pygame.display.set_caption('Memory ' +  v)

display = pygame.display.set_mode(screen_size)

puntuacion = 0 # Guardamos las parejas descubiertas

class Carta():
    def __init__(self,x,y,text,idImagen):
        self.x = x
        self.y = y
        self.text = text
        self.idImagen = idImagen
        self.isVisible = False
        self.isVolteado = False

    def getText(self):
        return self.text

    def isInside(self,x,y):
        # Comprombamos y la posicion (x,y) esta dentro de la carta
        if self.x < x < self.x + ANCHO_CARTA:
            if self.y < y < self.y + ANCHO_CARTA:
                return True
            
        return False

    def setVolteado(self, volteo):
        self.isVolteado = volteo

    def setVisible(self,estado):
        self.isVisible = estado

    def draw(self,screen):
        if self.isVisible or self.isVolteado:
            # mostramos la imagen
            screen.blit(images[self.idImagen],(self.x, self.y)) 
        else:
            # mostramos la interrogacion
            screen.blit(imagenOculto,(self.x, self.y)) 

cartas = []

idDibujos = [e for e in range(0,nFilas*nColumn // 2)] * 2

random.shuffle(idDibujos)

contador = 0
for i in range(0,nColumn):
    for j in range(0,nFilas):
        xPos = (ANCHO_CARTA + MARGEN_ENTRE_CARTAS) * i
        yPos = (ANCHO_CARTA + MARGEN_ENTRE_CARTAS) * j
        carta = Carta(xPos, yPos,
                      str(idDibujos[contador]), idDibujos[contador])
        cartas.append(carta)
        contador += 1

bRunning = True
bHayCambios = True
cartaVolteada1 = cartaVolteada2 = None
last_carta = None
while bRunning:

    for event in pygame.event.get():
        # Terminamos
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    if pygame.mouse.get_pressed()[0]: # hemos pulsado el boton izdo
        (mouse_x,mouse_y) = pygame.mouse.get_pos()
        for carta in  cartas:
            if carta.isInside(mouse_x,mouse_y) and last_carta != carta:
                last_carta = carta
                carta.setVolteado(True)
                if cartaVolteada1 == None: # es la primera volteada
                    cartaVolteada1 = carta
                else:                      # es la segunda volteada
                    cartaVolteada2 = carta 
                bHayCambios = True
                volteoSound.play()
                break
    
    if bHayCambios:
        print('repintando')
        display.fill(BLACK)
        for carta in cartas:
            carta.draw(display)
        if puntuacion == nFilas*nColumn//2 :
            puntos = ARIAL_100.render('¡¡GANÓ!!',True,WHITE)
        else:
            puntos = ARIAL_100.render('Puntos: '+str(puntuacion),True,WHITE)
        display.blit(puntos, (MARGEN_ENTRE_CARTAS, nFilas * (ANCHO_CARTA + MARGEN_ENTRE_CARTAS) - MARGEN_ENTRE_CARTAS))
        bHayCambios = False
        pygame.display.flip()
    
    if cartaVolteada1 != None and cartaVolteada2 != None: # 2 volteadas
        if cartaVolteada1.text == cartaVolteada2.text: # Iguales
            cartaVolteada2.setVisible(True)
            cartaVolteada1.setVisible(True)
            puntuacion += 1
        else:  # Distintas
            time.sleep(1.0) # damos un segundo para verlas ....
        cartaVolteada1.setVolteado(False)
        cartaVolteada2.setVolteado(False)
        cartaVolteada1 = cartaVolteada2 = None
        bHayCambios = True

