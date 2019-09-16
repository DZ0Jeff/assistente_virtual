import playsound
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import os
import datetime

MONTH = ['January','February','march','april',"may",'june','july','august','september','october','november','december']
DAYS = ["monday", 'tuesday','wednesday','thursday','friday','saturday','sunday']
DAYS_EXT = ["rd","th","st","nd"]


def play(text):
    playsound.playsound(text)


def speak(text):
    print('Iniciando...')
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


def get_audio():
    record = sr.Recognizer()
    print('Say something')
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


def get_date(text):
    text = text.lower()
    today = datetime.date.today()

    if text.count("today") > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTH:
            month = MONTH.index(word) - 1

        elif word in DAYS:
            day_of_week = DAYS.index(word)

        elif word.isdigit():
            day = int(word)

        else:
            for ext in DAYS_EXT:
                found = word.find(ext)

                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    if month < today.month and month != -1:
        year = year + 1
    
    if day < today.day and month == -1 and day != -1:
        month = month + 1 

    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday() # 0 - 6
        diference  = day_of_week - current_day_of_week

        if diference < 0:
            diference += 7 #go to next week
            if text.count("next") >= 1:
                diference += 7
        
        return today + datetime.timedelta(diference)

    if month == -1 and day == -1:
        return None
    else:
        return datetime.date(month=month, day=day, year=year)