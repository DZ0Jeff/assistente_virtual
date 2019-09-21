import playsound
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import subprocess
import datetime

def play(text):
    playsound.playsound(text)


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def googleSpeak(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    filename = "voice.mp3"
    print('Saving...')
    tts.save(f"Downloads/{filename}")
    play(f"Downloads/{filename}")
    print('DONE!')


def get_audio(debug=False):
    record = sr.Recognizer()
    print('Say something')
    with sr.Microphone() as src:
        audio = record.listen(src)
        said = ''

        try:
            said = record.recognize_google(audio)
            if debug:
                print(said)

        except Exception as error:
            print("[Erro] Audio não detectado ou erro na conexão" + str(error))

        except KeyboardInterrupt:
            print('Ação cancelada pelo usuario!')

    return said.lower()


def examples():
    speak("Hello")
    texto = get_audio()

    if "What is your name?" in texto:
        speak("My name is mud")

    elif "hello":
        speak('hellow, how are you?')


def note(text):
    date = datetime.datetime.now()
    filename = str(date).replace(":", "-") + "-note.txt"

    with open(filename, "w") as file:
        file.write(text)

    #git = "C:/Program Files (x86)/Git/bin/git.exe"
    #vscode_filepath = "C:/Users/JMS/AppData/Local/Programs/Microsoft VS Code/Code.exe"
    subprocess.Popen(["notepad.exe", filename])
