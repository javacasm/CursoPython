# Basado en Animal.py by Chris Meyers and Fred Obermann Python4fun
# http://openbookproject.net/py4fun/animal/animal.py
# 

v = '0.5'

iTexto = 0
iRespuestaSi = 1
iRespuestaNo = 2
iSinConexion = -1

ficheroDatos = 'elementos.txt'


class Nodo :
    """
    Cada nodo guarda una pregunta o una respuesta
    Si es una pregunta apunta a un nodo si la respuesta es Sí y a otro si es No
    Los nodos que son respuetas no apuntan a ningún otro nodo
    """
    def __init__ (self, texto, idNodo, nodoSi = None, nodoNo = None) : # Por defecto es una respuesta
        self.texto   = texto # Guardamos la pregunta o la respuesta
        self.nodoSi  = nodoSi
        self.nodoNo   = nodoNo
        self.idNodo  = idNodo

    def setText(self, texto):
        self.texto = texto

    def setRespuestas(self, nodoSi, nodoNo):
        self.nodoSi  = nodoSi
        self.nodoNo  = nodoNo

    def isPregunta(self):
        return self.nodoSi != None

    def __str__(self):
        if self.isPregunta():
            strElement = '%d:%s:%d:%d\n'%(self.idNodo, self.texto,self.nodoSi.idNodo, self.nodoNo.idNodo)
        else:
            strElement = '%d:%s:%d:%d\n'%(self.idNodo, self.texto,iSinConexion,iSinConexion)        
        return strElement

    def __eq__(self, otroNodo):
        if otroNodo == None:
            return False
        return self.idNodo == otroNodo.idNodo and self.texto == otroNodo.texto

    def __lt__(self, otroNodo):
        return self.idNodo < otroNodo.idNodo

class Respuesta(Nodo):
    def __init__(self,nuevaCosa, idNodo):
        ## eliminamos el artículo si estuviera
        for art in ['el','la','los','las','un','una','unos','unas']:
            if nuevaCosa.startswith(art + ' '):
                print('# quitando ' + art)
                nuevaCosa = nuevaCosa[len(art) + 1:]    
                break # no creo que haya más artículos    
        super().__init__( nuevaCosa, idNodo, None, None)


class Pregunta(Nodo):
    def __init__(self, pregunta, idNodo, nodoSi, nodoNo):
        if pregunta[0] == '¿' : pregunta = pregunta[1:]
        if pregunta[-1] == '?': pregunta = pregunta[:-1]        
        super().__init__( pregunta, idNodo, nodoSi = nodoSi, nodoNo = nodoNo)


# Basado en Animal.py by Chris Meyers and Fred Obermann Python4fun
# http://openbookproject.net/py4fun/animal/animal.py
# 

import os, time

v = '0.9'

def getRespuesta (pregunta) :
    """
    Mostrarmos la pregunta y esperamos la respuesta
    Cualquier respuesta que empiece con 's' es Sí, el resto No
    Devuelve True para Sí, False para No
    """
    respuesta = input (pregunta)
    if respuesta == 'dump':
        dumpElementos()    
    respuestaProcesada = respuesta[0:1].lower() # Convertimos a minúscula y nos quedamos con la primera letra
    if respuestaProcesada == 's' : 
        return True
    else: 
        return False


elementos = []


def buscaNodobyId(id):
    for nodo in elementos:
        if nodo.idNodo == id:
            return nodo
    print(f'No se encontró el nodo {id}')
    return None


def cargaElementos():
    global elementos
    if ficheroDatos in os.listdir(): # si existe lo cargamos
        f = open(ficheroDatos,'r')
        lineas = f.readlines()
        lineas.reverse() # Para empezar por los últimos añadidos que serán Respuestas
        nRespuestas = nPreguntas = 0
        for linea in lineas:
            if linea[0] == '#': # es un comentario
                continue
            linea = linea.strip() # eliminamos el final de línea
            datos = linea.split(':')
            if len(datos) == 4:
                if datos[3] == datos[2] == str(iSinConexion): # Es una respuesta
                    nodo = Respuesta(datos[1], int(datos[0]))
                    nRespuestas += 1
                else: # Es una pregunta
                    idSi = int(datos[2])
                    nodoSi = buscaNodobyId(idSi)
                    idNo = int(datos[3])
                    nodoNo = buscaNodobyId(idNo)
                    idNodo = int(datos[0])
                    nodo = Pregunta(datos[1],idNodo, nodoSi, nodoNo)
                    nPreguntas += 1
                elementos.append(nodo) 
            else:
                print('Error recuperando datos:',datos )
        elementos.reverse() # La invierto para que esté en el orden antural
        print(f'Recuperados {len(elementos)} elementos: {nRespuestas} respuestas y {nPreguntas} preguntas.')
    else:
        print('No se encontraron datos anteriores... Creando desde 0')
        elementos.append(Respuesta('Geranio',0)) 

def guardaElementos():
    global elementos    
    if ficheroDatos in os.listdir(): # si existe lo renombramos
        strTime = time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime())
        os.rename(ficheroDatos,ficheroDatos+strTime+'.txt')
    f = open(ficheroDatos ,'wt')
    f.write("#id:text:Si:No\n")
    elementos_ordenados = sorted(elementos)
    for nodo in elementos_ordenados:
        f.write(str(nodo))
    f.close()
    print(f'Guardados {len(elementos)} nodos')

def dumpElementos(): # Lo utilizamos como depuración para ver que funciona
    contador = 0
    print("id\t\t\ttext\tSi\tNo")
    #for e in elementos:
    for texto,idSi,idNo in elementos:
        #print('%d\t%s\t%d\t%d'%(contador,e[iTexto],e[iRespuestaSi],e[iRespuestaNo]))
        print('%d\t%s\t%d\t%d'%(contador, texto, idSi, idNo))
        contador += 1

def getRespuesta (pregunta) :
    """
    Mostrarmos la pregunta y esperamos la respuesta
    Cualquier respuesta que empiece con 's' es Sí, el resto No
    Devuelve True para Sí, False para No
    """
    respuesta = input (pregunta)
    respuestaProcesada = respuesta[0:1].lower() # Convertimos a minúscula y nos quedamos con la primera letra
    if respuestaProcesada == 's' : 
        return True
    else: 
        return False


def main () :
    """
    Juego de las 20 preguntas, si no acierto, pide una pregunta para distinguir
    """

    print('JUEGO DE LAS 20 PREGUNTAS\n')

    cargaElementos()

    while True : ## Bucle principal del juego

        nodoActual = buscaNodobyId(0)  # Empezamos con el nodo raiz
   
        print('Piense en una cosa...\n')

        # Bucle de adivinación: Nos vamos moviendo por todo el árbol según sea la respuesta
        # hasta llegar a un nodo que no tenga enlaces que será una respuesta
        lastNodo = None 
        while nodoActual.isPregunta() :
            lastNodo = nodoActual # nos sirve para buscar el padre del actual nodo si tenemos que cambiarlos
            if getRespuesta('¿' + nodoActual.texto + '? ') == True : ## Nos movemos al siguiente nodo según sea la respuesta
                nodoActual = nodoActual.nodoSi 
            else : 
                nodoActual = nodoActual.nodoNo
        
        # No hay más preguntas... tenemos la respuesta
        if getRespuesta('¿Es un ' + nodoActual.texto + '? ') :  # Hemos acertado
            print('¡¡Acerté!!')
            continue ## Volvemos al bucle principal
        
        ## La respuesta no es correcta
        nuevaCosa = input ('¿Qué es? ')
        pregunta  = input ('¿Qué puedo preguntar para distinguir %s de %s? '
                                  % (nuevaCosa,nodoActual.texto))

        # Vamos a crear 2 nodos:
        #  * uno con la nueva Respuesta 
        #  * otro con la pregunta
        nuevaRespuesta = Respuesta(nuevaCosa,len(elementos))
        elementos.append(nuevaRespuesta)
        # le ponemos el idNodo de la anterior respuesta para mantenerlos "ordenados"
        if not getRespuesta('Si fuera %s ¿la respuesta sería? ' % nuevaCosa) :
            nuevoPregunta = Pregunta(pregunta, nodoActual.idNodo, nodoActual, nuevaRespuesta)
        else:
            nuevoPregunta = Pregunta(pregunta, nodoActual.idNodo, nuevaRespuesta, nodoActual)

        nodoActual.idNodo = len(elementos) # Lo ponemos en la última posición
        elementos.append(nuevoPregunta)
        
        # Vamos a buscar quien apunta
        if lastNodo.nodoSi == nodoActual:
            lastNodo.nodoSi = nuevoPregunta
        elif lastNodo.nodoNo == nodoActual:
            lastNodo.nodoNo = nuevoPregunta
        else:
            print('Tenemos un problema') 
        guardaElementos()

        # Preguntamos si queremos seguir jugando
        if getRespuesta("¿Quieres pensar en una cosa? ") == False : 
            print('¡Adiós!')
            break # Terminamos


if __name__ == "__main__" : main ()