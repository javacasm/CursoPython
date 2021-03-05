# joshua 20 Questions

import pyttsx3
import Preguntas20

def main():
    engine = pyttsx3.init()
    engine.setProperty('voice','spanish') 

    juego = Preguntas20.Juego20()
    pregunta ='Hola Profesor Falken '
    while True:
        engine.say(pregunta)
        print(pregunta + ' ',end ='')
        engine.runAndWait()
        respuesta = input()
        pregunta = juego.updateEstado(respuesta)

if __name__ == '__main__':
    main()