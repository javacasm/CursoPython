'''
@joshua by War Games....

pyttsx3 pypi.org/project/pyttsx3
py Text To Speak 3

Linux - sudo apt instal espeak
Windows - SAPI5
Mac - NSSpeechSynthesizer

pip3 install pyttsx3

Doc -  https://pyttsx3.readthedocs.io/en/latest/engine.html

'''



import pyttsx3
import Preguntas20

def main():
    engine = pyttsx3.init()
    message = 'Grettings Professor Falken. Would you want to play?'
    engine.say(message)
    engine.runAndWait()

    voces = engine.getProperty('voices')
    for voz in voces:
        print(voz)
    
    
    velocidad = engine.getProperty('rate')
    engine.setProperty('rate',velocidad * 2)
    print('velocidad * 2' )
    engine.say(message)
    engine.runAndWait()
    
    volumen = engine.getProperty('volume')
    engine.setProperty('volume',volumen / 2)
    print('volume/2')
    engine.say(message)
    engine.runAndWait()
    
    fichero = 'joshua.mp3'
    engine.setProperty('volume', volumen)
    engine.setProperty('rate', velocidad)
    engine.save_to_file(message, fichero)
    engine.runAndWait()
    print('Guardado el fichero '+ fichero)
    
    engine.setProperty('voice','spanish') 
    engine.say('Hola profesor Falken. ¿Quiere jugar?')
    engine.runAndWait()
    
    engine.stop()
    
if __name__ == '__main__':
    main()
