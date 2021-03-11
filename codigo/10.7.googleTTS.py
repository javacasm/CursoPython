# install playsound (para reproducir los ficheros mp3
# https://www.techwithtim.net/tutorials/voice-assistant/playing-sound/
# install PyAudio sudo apt-get install python-pyaudio python3-pyaudio
# pyaudio 

# install gtts https://pypi.org/project/gTTS/
#ejemplo de https://people.csail.mit.edu/hubert/pyaudio/

import gtts
tts = gtts.gTTS('hola cara de bola', lang='es', tld='es')
tts.save('carabola.mp3')

''' 
from gtts import gTTS
from io import BytesIO
mp3_fp = BytesIO()
tts = gTTS('hello', lang='en')
tts.write_to_fp(mp3_fp)
''' 

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = '/tmp/voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)



# Play sound with pyaudio
# https://stackoverflow.com/questions/51091577/playing-audio-directly-from-a-python-program-text-to-speech