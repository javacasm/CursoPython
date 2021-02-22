# Basado en Animal.py by Chris Meyers and Fred Obermann Python4fun
# http://openbookproject.net/py4fun/animal/animal.py
# 

v = '0.5'

def getRespuesta (pregunta) :
    """
    Mostrarmos la pregunta y esperamos la respuesta
    Cualquier respuesta que empiece con 's' es Sí, el resto No
    Devuelve True para Sí, False para No
    """
    respuesta = input (pregunta)
    if respuesta == 'dump':
        dumpElementos()
    # Convertimos a minúscula y nos quedamos con la primera letra
    respuestaProcesada = respuesta[0:1].lower() 
    if respuestaProcesada == 's' : 
        return True
    else: 
        return False

iTexto = 0
iRespuestaSi = 1
iRespuestaNo = 2
iSinConexion = -1

elementos = [ ['geranio', iSinConexion, iSinConexion] ] # elemento, respuestaSi, respuestaNo

def dumpElementos(): # Lo utilizamos como depuración para ver que funciona
    contador = 0
    print("id\t\t\ttext\tSi\tNo")
    #for e in elementos:
    for texto,idSi,idNo in elementos:
        #print('%d\t%s\t%d\t%d'%(contador,e[iTexto],e[iRespuestaSi],e[iRespuestaNo]))
        print('%d\t%s\t%d\t%d'%(contador, texto, idSi, idNo))
        contador += 1

def main () :
    """
    Juego de las 20 preguntas, si no acierto, pido una pregunta para distinguir
    """
    
    while True : # Bucle principal del juego

        nodoActual = 0 # Empezamos con el nodo raiz

        print('Piense en una cosa...')

        # Bucle de adivinación: Nos vamos moviendo por todo el árbol según sea la respuesta
        # hasta llegar a un nodo que no tenga enlaces que será una respuesta

        while elementos[nodoActual][iRespuestaSi] != iSinConexion : # Es una pregunta
            # Nos movemos al siguiente nodo según sea la respuesta
            if getRespuesta('¿' + elementos[nodoActual][iTexto] + '? ') == True :
                nodoActual = elementos[nodoActual][iRespuestaSi]
            else : 
                nodoActual = elementos[nodoActual][iRespuestaNo]
        
        hipotesis = elementos[nodoActual][iTexto]  # vamos a usarlo muchas veces, mejor "cachearlo"

        # No hay más preguntas... tenemos la respuesta
        if getRespuesta('¿Es un ' + hipotesis + '? ') :  # Hemos acertado
            print('¡¡Acerté!!')
        else:        # La respuesta no es correcta
            nuevaCosa = input ('¿Qué es? (no incluya articulos) ')
            pregunta  = input ('¿Qué puedo preguntar para distinguir %s de %s? '% (nuevaCosa, hipotesis))

            # eliminamos los signos de interrogación si los hubiera
            if pregunta[0] == '¿' : pregunta = pregunta[1:] # Primer caracter es ¿
            if pregunta[-1] == '?': pregunta = pregunta[:-1] # Ultimo caracter es ?

            posicionActual = len(elementos) # Sera el ultimo elemento por ahora
            # añadimos nuestra hipotesis 
            elementos.append([hipotesis, iSinConexion, iSinConexion]) 
            
            #añadimos la nueva cosa que sera la ultima
            posicionNuevo = len(elementos) 
            elementos.append([nuevaCosa,iSinConexion,iSinConexion])
            
            if not getRespuesta('Si fuera %s ¿la respuesta sería? ' % nuevaCosa) :
                elementos[nodoActual][iRespuestaSi] = posicionActual
                elementos[nodoActual][iRespuestaNo] = posicionNuevo
            else:
                elementos[nodoActual][iRespuestaSi]  = posicionNuevo
                elementos[nodoActual][iRespuestaNo]  = posicionActual

            elementos[nodoActual][iTexto] = pregunta
        
        # Preguntamos si queremos seguir jugando
        if getRespuesta("¿Quieres pensar en otra cosa? ") == False : 
            print('¡Adiós y gracias por jugar conmigo!')
            break # Terminamos


if __name__ == "__main__" : main ()