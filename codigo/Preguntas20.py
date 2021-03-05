'''
Version 100% Orientada a objetos
Clases: Nodo, Respuesta y Pregunta
Clase : Juego20
'''
import os, time

iTexto = 0
iRespuestaSi = 1
iRespuestaNo = 2
iSinConexion = -1

class Nodo :
    """
    Cada nodo guarda una pregunta o una respuesta
    Si es una pregunta apunta a un nodo si la respuesta es Sí y a otro si es No
    Los nodos que son respuetas no apuntan a ningún otro nodo
    """
    v = '0.9.4'
    def __init__ (self, texto, idNodo, nodoSi = None, nodoNo = None) : # Por defecto es una respuesta
        self.texto   = texto # Guardamos la pregunta o la respuesta
        self.nodoSi  = nodoSi
        self.nodoNo  = nodoNo
        self.idNodo  = idNodo
        self.parent  = None
        self.bDebug   = False # se activan mas trazas

    def setParent(self, padre):
        self.parent = padre
        if self.bDebug:
            print(f'Soy "{self.texto}" y "{padre.texto}" es mi padre')

    def setText(self, texto):
        self.texto = texto

    def setRespuestas(self, nodoSi, nodoNo):
        self.nodoSi  = nodoSi
        self.nodoNo  = nodoNo

    def isPregunta(self):
        return self.nodoSi != None

    def __str__(self):
        # Conversion a cadena
        if self.isPregunta():
            strElement = '%d:%s:%d:%d'%(self.idNodo, self.texto,self.nodoSi.idNodo, self.nodoNo.idNodo)
        else:
            strElement = '%d:%s:%d:%d'%(self.idNodo, self.texto,iSinConexion,iSinConexion)        
        return strElement

    def __eq__(self, otroNodo):
        # operador igualdad
        if otroNodo == None:
            return False
        return self.idNodo == otroNodo.idNodo and self.texto == otroNodo.texto

    def __lt__(self, otroNodo):
        # operador < para ordenacion
        return self.idNodo < otroNodo.idNodo

class Respuesta(Nodo):
    def __init__(self, nuevaCosa, idNodo):
        nuevaCosa = nuevaCosa.lower() # Todo minusculas
        ## eliminamos artículo y 'es' si estuviera
        for art in ('es', 'el','la','los','las','un','una','unos','unas'):
            if nuevaCosa.startswith(art + ' '):
                print('# quitando ' + art)
                nuevaCosa = nuevaCosa[len(art) + 1:]    
                break # no creo que haya más artículos    
        super().__init__( nuevaCosa, idNodo, None, None)
        if self.bDebug:
           print(f'Respuesta: "{self.texto}"')


class Pregunta(Nodo):
    def __init__(self, pregunta, idNodo, nodoSi, nodoNo):
        pregunta = pregunta.lower()  # Todo minusculas
        if pregunta[0] == '¿' : pregunta = pregunta[1:]
        if pregunta[-1] == '?': pregunta = pregunta[:-1]        
        super().__init__( pregunta, idNodo, nodoSi = nodoSi, nodoNo = nodoNo)
        if self.bDebug:
            print(f'Pregunta "{self.texto}" Si: "{nodoSi.texto}" No: "{nodoNo.texto}"')


class Juego20():
    '''
    Juego de las 20 preguntas
    Utiliza una máquina de estados
    '''

    # estados
    eNoEstado = -1 
    eQuieresJugar = 0
    ePregunta = 1
    eHipotesis = 2
    eQueEs = 3
    ePreguntaDiferencia = 4
    eRespuestaNuevo = 5
    eActualizaArbol = 6

    def __init__(self, ficheroDatos = 'nodos.txt'):
        self.ficheroDatos = ficheroDatos
        self.nodos = []
        self.v = '0.9.3'
        self.estado = Juego20.eNoEstado
        self.detallesEstado = []
        self.bDebug = True
        
        print(f'Juego20 v{self.v} & nodo v{Nodo.v}')
        self.cargaNodos()

    def procesaRespuestaSN (self, respuesta) :
        """
        Cualquier respuesta que empiece con 's' o 'y' es Sí, el resto No
        Devuelve True para Sí, False para No
        """
        respuesta = respuesta.lower()
        if respuesta == 'dump':  # Hace un volcado de los datos si se envia 'dump'
            self.dumpNodos()
            return False
        if respuesta in ('vale', 'claro', 'bueno', 'ok'):
            respuesta = 's'
        respuestaProcesada = respuesta[0:1] # Convertimos a minúscula y nos quedamos con la primera letra
        if respuestaProcesada in ('s','y') : 
            return True
        else: 
            return False

    def buscaNodobyId(self, id):
        # busca un nodo por su id
        for nodo in self.nodos:
            if nodo.idNodo == id:
                return nodo
        print(f'No se encontró el nodo {id}')
        return None

    def cargaNodos(self, fichero = None):
        '''
        Recupera los nodos desde fichero
        Formato idNodo:texto:idNodoSi:idNodoNo
        '''
        if fichero == None:
            fichero = self.ficheroDatos
            
        if fichero in os.listdir(): # si existe lo cargamos
            f = open(fichero, 'rt')
            lineas = f.readlines()
            f.close()
            lineas.reverse() # Para empezar por los últimos añadidos que serán Respuestas
            nRespuestas = nPreguntas = 0
            # Primero las respuestas
            for linea in lineas: 
                if linea[0] == '#': # es un comentario
                    continue
                linea = linea.strip() # eliminamos el final de línea
                datos = linea.split(':')
                if len(datos) == 4:
                    texto = datos[1]
                    idNodo = int(datos[0])
                    if datos[3] == datos[2] == str(iSinConexion): # Es una respuesta
                        nodo = Respuesta(texto, idNodo)
                        nRespuestas += 1
                        self.nodos.append(nodo) 
                else:
                    print('Error recuperando datos:',datos )
            # Ahora las preguntas
            for linea in lineas: 
                if linea[0] == '#': # es un comentario
                    continue
                linea = linea.strip() # eliminamos el final de línea
                datos = linea.split(':')
                if len(datos) == 4:
                    texto = datos[1]
                    idNodo = int(datos[0])
                    if datos[3] == datos[2] == str(iSinConexion): # Es una respuesta
                        pass
                    else:                      # Es una pregunta
                        idSi = int(datos[2])
                        nodoSi = self.buscaNodobyId(idSi)
                        idNo = int(datos[3])
                        nodoNo = self.buscaNodobyId(idNo)
                        if nodoSi == None or nodoNo == None:
                            print('Error recuperando datos')
                            break
                        nodo = Pregunta(texto, idNodo, nodoSi, nodoNo)
                        nodoSi.setParent(nodo)
                        nodoNo.setParent(nodo)
                        nPreguntas += 1
                        self.nodos.append(nodo) 
                else:
                    print('Error recuperando datos:',datos )      
            self.nodos.reverse() # La invierto para que esté en el orden antural
            print(f'Recuperados {len(self.nodos)} elementos: {nRespuestas} respuestas y {nPreguntas} preguntas de {fichero}')
        else:
            print('No se encontraron datos anteriores... Creando desde 0')
            self.nodos.append(Respuesta('Geranio',0)) 

    def guardaNodos(self,fichero = None):
        '''
        Guarda los nodos en fichero
        Formato idNodo:texto:idNodoSi:idNodoNo
        '''
        strResultado=''
        if fichero == None:
            fichero = self.ficheroDatos
            
        if fichero in os.listdir(): # si existe lo renombramos
            strTime = time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime())
            os.rename(fichero, fichero + strTime + '.txt')
        f = open(fichero ,'wt')
        f.write("#id:text:Si:No\n")
        elementos_ordenados = sorted(self.nodos)
        preguntas = 0
        respuestas = 0
        for nodo in elementos_ordenados:
            if nodo.isPregunta(): preguntas += 1
            f.write(str(nodo)+'\n')
        f.close()
        strResultado = f'Guardados {len(self.nodos)} nodos en {fichero} \n'
        strResultado += f'Ya se {preguntas} cosas'
        print(strResultado)
        return strResultado

    def dumpNodos(self): # Lo utilizamos como depuración para ver que funciona
        print("id\t\t\ttext\tSi\tNo")
        for nodo in self.nodos:
            print(str(nodo))

    def getPreguntaFromNodo(self, nodo):
        if len(self.detallesEstado) == 0:
            self.detallesEstado.append(nodo)
        else:
            self.detallesEstado[0] = nodo
        if nodo.isPregunta():
            self.estado = Juego20.ePregunta   # Hacemos otra pregunta
            pregunta = f'¿{nodo.texto}?'
        else:
            self.estado = Juego20.eHipotesis   # Creemos que es ...
            pregunta = f'¿es {nodo.texto}?'
        return pregunta

    def updateEstado(self, mensaje):
        respuesta = ''
        if  self.estado == Juego20.eNoEstado:                    # Estado inicial
            respuesta = 'Hola\n¿Quieres Jugar a las 20 Preguntas?'
            self.estado = Juego20.eQuieresJugar
            self.detallesEstado.clear()
        elif self.estado == Juego20.eQuieresJugar:               # ¿Quieres jugar?
            if self.procesaRespuestaSN(mensaje):
                nodoInicial = self.buscaNodobyId(0)
                respuesta = 'Piensa una cosa...\n\n'
                respuesta += self.getPreguntaFromNodo(nodoInicial)
            else:
                self.estado = Juego20.eNoEstado
                respuesta = 'Ok, otro día sera'
                self.detallesEstado.clear()            
        elif self.estado == Juego20.ePregunta:                  # Hacemos preguntas
            if self.procesaRespuestaSN(mensaje):
                nuevoNodo = self.detallesEstado[0].nodoSi
            else:
                nuevoNodo = self.detallesEstado[0].nodoNo
            self.detallesEstado[0] = nuevoNodo
            respuesta = self.getPreguntaFromNodo(nuevoNodo)
        elif self.estado == Juego20.eHipotesis:                 #  hipotesis
            if self.procesaRespuestaSN(mensaje):
                respuesta = '¡¡ACERTÉ!!\n\n¿Quieres Jugar a las 20 Preguntas?'
                self.estado = Juego20.eQuieresJugar
                self.detallesEstado.clear()
            else:
                respuesta = '¿Qué es?'           
                self.estado = Juego20.eQueEs
        elif self.estado == Juego20.eQueEs:                     # Aprender algo
            self.estado = Juego20.ePreguntaDiferencia
            respuesta = f'¿Qué puedo preguntar para diferenciar {mensaje} de {self.detallesEstado[0].texto}?'
            self.detallesEstado.append(mensaje) #detal[0]:actual detal[1]:nuevaCosa
        elif self.estado == Juego20.ePreguntaDiferencia:        # Nueva pregunta
            respuesta = f'Para un {self.detallesEstado[1]} ¿la respuesta sería?'
            self.detallesEstado.append(mensaje) #detal[0]:actual detal[1]:nuevaCosa detal[2]:nuevaPregunta
            self.estado = Juego20.eRespuestaNuevo
        elif self.estado == Juego20.eRespuestaNuevo:            # Respuesta Nueva cosa
            # creamos la nueva respuesta
            respuestaActual = self.detallesEstado[0]
            respuestaNueva = Respuesta(self.detallesEstado[1], len(self.nodos))
            self.nodos.append(respuestaNueva)
            # creamos la nueva pregunta
            if self.procesaRespuestaSN(mensaje): # Para el nuevo es si
                nuevaPregunta = Pregunta(self.detallesEstado[2], len(self.nodos), respuestaNueva, respuestaActual)
            else: # Para el nuevo no
                nuevaPregunta = Pregunta(self.detallesEstado[2], len(self.nodos), respuestaActual, respuestaNueva)
            self.nodos.append(nuevaPregunta)
            self.detallesEstado.clear()
            # ponemos la nueva pregunta donde estaba la antigua respuesta
            if respuestaActual.parent != None:
                if respuestaActual.parent.nodoSi == respuestaActual:
                    respuestaActual.parent.nodoSi = nuevaPregunta
                elif respuestaActual.parent.nodoNo == respuestaActual:
                    respuestaActual.parent.nodoNo = nuevaPregunta
                else:
                    print('Tenemos un problema')
                    self.dumpNodos()
            else:
                print('Tenemos un problema')
                self.dumpNodos()
                            
            resultadoGuardar = self.guardaNodos()
            
            self.estado = Juego20.eQuieresJugar
            respuesta = 'Entendido\n\n¿Quieres Jugar a las 20 Preguntas?'
        elif self.estado == Juego20.eActualizaArbol:                # Guardamos
            respuesta = 'Añadido otro mas'
        else:
            respuesta = 'Error en la codificación de los estados'
            print(respuesta)
            
        return respuesta


if __name__ == '__main__':
    juego = Juego20('nodos_Javacasm.txt')
    pregunta ='¡Hola! '
    while True:
        try:
            respuesta = input(pregunta + ' ')
            pregunta = juego.updateEstado(respuesta)
        except:
            print('bye')