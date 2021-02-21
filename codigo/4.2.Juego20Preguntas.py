# Basado en Animal.py by Chris Meyers and Fred Obermann Python4fun
# http://openbookproject.net/py4fun/animal/animal.py
# 

v = '0.1'

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

elementos = [['geranio',-1,-1]] # elemento, respuestaSi, respuestaNo

def dumpElementos(): # Lo utilizamos como depuración para ver que funciona
    contador = 0
    print("id\ttext\tSi\tNo")
    for e in elementos:
        print('%d\t%s\t%d\t%d'%(contador,e[0],e[1],e[2]))
        contador += 1

def main () :
    """
    Juego de las 20 preguntas, si no acierto, pide una pregunta para distinguir
    """
    
    while True : ## Bucle principal del juego

        nodoActual = 0 # Empezamos con el nodo raiz

        print('Piense en una cosa...')

        # Bucle de adivinación: Nos vamos moviendo por todo el árbol según sea la respuesta
        # hasta llegar a un nodo que no tenga enlaces que será una respuesta

        while elementos[nodoActual][1] != -1 : # Es una pregunta
            if getRespuesta('¿' + elementos[nodoActual][0] + '? ') == True : ## Nos movemos al siguiente nodo según sea la respuesta
                nodoActual = elementos[nodoActual][1]
            else : 
                nodoActual = elementos[nodoActual][2]
        
        hipotesis = elementos[nodoActual][0]  # vamos a usarlo muchas veces, mejor "cachearlo"

        # No hay más preguntas... tenemos la respuesta
        if getRespuesta('¿ Es un ' + hipotesis + '? ') :  # Hemos acertado
            print('¡¡Acerté!!')
            continue ## Volvemos al bucle principal
        
        ## La respuesta no es correcta
        nuevaCosa = input ('¿Qué es? ')
        pregunta  = input ('¿Qué puedo preguntar para distinguir %s de %s? '% (nuevaCosa, hipotesis))

        ## eliminamos los signos de interrogación si los hubiera
        if pregunta[0] == '¿' : pregunta = pregunta[1:]
        if pregunta[-1] == '?': pregunta = pregunta[:-1]

        posicionActual = len(elementos)
        elementos.append([hipotesis, -1, -1])
        posicionNuevo = len(elementos)
        elementos.append([nuevaCosa,-1,-1])
        if not getRespuesta('Si fuera %s ¿la respuesta sería? ' % nuevaCosa) :
            elementos[nodoActual][1] = posicionActual
            elementos[nodoActual][2] = posicionNuevo
        else:
            elementos[nodoActual][1]  = posicionNuevo
            elementos[nodoActual][2]  = posicionActual

        elementos[nodoActual][0] = pregunta
        
        # Preguntamos si queremos seguir jugando
        if getRespuesta("¿Quieres pensar en otra cosa? ") == False : 
            print('¡Adiós!')
            break # Terminamos


if __name__ == "__main__" : main ()