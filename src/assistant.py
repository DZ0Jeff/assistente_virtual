import playsound
import speech_recognition as sr
from gtts import gTTS
import os
import time


def play(text):
    playsound.playsound(text)


def speak(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    filename = "voice.mp3"
    print('Saving...')
    tts.save(f"Downloads/{filename}")
    play(f"Downloads/{filename}")
    print('DONE!')


def get_audio():
    record = sr.Recognizer()
    with sr.Microphone() as src:
        audio = record.listen(src)
        said = ''

        try:
            said = record.recognize_google(audio)
            print(said)

        except Exception as error:
            print("[Erro] Audio não detectado ou erro na conexão" + str(error))

        except KeyboardInterrupt:
            print('Ação cancelada pelo usuario!')

    return said


def examples():
    speak("Hello")
    texto = get_audio()


    if "What is your name?" in texto:
        speak("My name is mud")

    elif "hello":
        speak('hellow, how are you?')

    else:
        speak("I don't understand what you are talking about, please, try again")