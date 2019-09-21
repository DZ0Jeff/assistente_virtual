from src.assistant import speak, play, get_audio, googleSpeak, note
from src.files import create_file, read_file
from src.google_calendar import get_date, authenticate_google, get_events
from time import sleep


def main():
    WAKE = "start"
    service = authenticate_google()
    print('=' * 40, 'Genesis Virtual Assist', '=' * 40)

    while True:
        print('Listening...')
        init = get_audio()

        if init.count(WAKE) > 0:
            speak('I am Ready')
            #option = int(input('Text[1] speak[2]: '))
            #text = input("Option: ") if option == 1 else get_audio()
            text = get_audio()
            print(text)

            #Calendar
            CALENDAR_STRS = ["what i do have", "do i have plans", "am i busy"]
            for phrase in CALENDAR_STRS:
                if phrase in text:
                    date = get_date(text)
                    if date:
                        
                        get_events(date, service)
                    else:
                        speak("I Don't understand, try again")

            #note
            NOTE_STRS = ["make a note", "write this down", "remember this"]
            for phrase in NOTE_STRS:
                if phrase in text:
                    speak("What you would like to make a note? ")
                    note_text = get_audio()
                    note(note_text)
                    speak("I've made a note on that")

            QUIT_STRS = ["quitting","quit","done"]
            for phrase in QUIT_STRS:
                if phrase in text:
                    speak("Too Soon... Bye, come back")
                    sleep(3)
                    exit()    


if __name__ == "__main__":
    main()
