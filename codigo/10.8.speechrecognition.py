# speech recosnition https://www.techwithtim.net/tutorials/voice-assistant/getting-microphone-input/


# pip3 install AudioSegment
# pip3 install speech_recognition


import os
from pathlib import Path

from pydub import AudioSegment 
import speech_recognition as sr

TMP= Path(os.getenv("TMP", "/tmp"))

def get_text_from_audio_file(file: Path) -> str: 
    sound= AudioSegment.from_mp3(str(file)) 
    transcript_wav = TMP / "transcript.wav" 
    print(f'tempfile: {transcript_wav}')
    sound.export(str(transcript_wav), format="wav")

    recognizer = sr.Recognizer()

    with sr.AudioFile(str(transcript_wav)) as source:
        audio = recognizer.record(source)
        ret = recognizer.recognize_google(audio, show_all = True)

    transcript_wav.unlink()

    return ret["alternative"][0]["transcript"]


'''
from alarm.alarm import countdown_and_play_alarm 
from alarm.audio import create_alarm_audio_file

def test_voice_alarm_text():

    file = create_alarm_audio_file("take the trash out") 
    countdown_and_play_alarm(0, file, timeout=2) 
    actual = get_text_from_audio_file(file) 
    expected = "take the trash out take the trash out take the trash out"

    assert actual == expected 

    Path(file).unlink()

'''
txt = get_text_from_audio_file('/home/javacasm/Descargas/dumbtest.mp3')

print(f'got: {txt}')