# Basado en Animal.py by Chris Meyers and Fred Obermann Python4fun
# http://openbookproject.net/py4fun/animal/animal.py
# 

v = '0.1'

class Nodo :
    """
    Cada nodo guarda una pregunta o una respuesta
    Si es una pregunta apunta a un nodo si la respuesta es Sí y a otro si es No
    Los nodos que son respuetas no apuntan a ningún otro nodo
    """
    def __init__ (self, texto, nodoSi=None, nodNo=None) : # Por defecto es una respuesta
        self.texto   = texto # Guardamos la pregunta o la respuesta
        self.nodoSi  = nodoSi
        self.nodNo   = nodNo

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

nodoInicial = Nodo("Geranio")

def main () :
    """
    Juego de las 20 preguntas, si no acierto, pide una pregunta para distinguir
    """

    while True : ## Bucle principal del juego

        # Preguntamos si queremos seguir jugando
        if getRespuesta("¿Quieres pensar en una cosa? ") == False : 
            print('¡Adiós!')
            break # Terminamos

        nodoActual = nodoInicial # Empezamos con el nodo raiz

        # Bucle de adivinación: Nos vamos moviendo por todo el árbol según sea la respuesta
        # hasta llegar a un nodo que no tenga enlaces que será una respuesta

        while nodoActual.nodoSi != None : # Es una pregunta
            if getRespuesta('¿' + nodoActual.texto + '? ') == True : ## Nos movemos al siguiente nodo según sea la respuesta
                nodoActual = nodoActual.nodoSi 
            else : 
                nodoActual = nodoActual.nodoNo
        
        # No hay más preguntas... tenemos la respuesta
        if getRespuesta('¿ Es un ' + nodoActual.texto + '? ') :  # Hemos acertado
            print('¡¡Acerté!!')
            continue ## Volvemos al bucle principal
        
        ## La respuesta no es correcta
        nuevaCosa = input ('¿Qué es? ')
        pregunta  = input ('¿Qué puedo preguntar para distinguir %s de %s? '
                                  % (nuevaCosa,nodoActual.texto))

        ## eliminamos los signos de interrogación si los hubiera
        if pregunta[0] == '¿' : pregunta = pregunta[1:]
        if pregunta[-1] == '?': pregunta = pregunta[:-1]

        if not getRespuesta('Si el animal fuera %s ¿la respuesta sería? ' % nuevaCosa) :
            nodoActual.nodoNo = Nodo(nuevoAnimal)
            nodoActual.nodoSi = Nodo(nodoActual.texto)
        else:
            nodoActual.nodoSi = Nodo(nuevoAnimal)
            nodoActual.nodoNo = Nodo(nodoActual.texto)

        nodoActual.texto = pregunta


if __name__ == "__main__" : main ()