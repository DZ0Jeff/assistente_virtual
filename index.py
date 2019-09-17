from src.assistant import speak, play, get_audio, get_date, googleSpeak
from src.files import create_file, read_file
from src.google_calendar import authenticate_google, get_events


def main():
    print('=' * 40, 'Genesis Virtual Assist', '=' * 40)

    option = int(input('Text[1] speak[2]: '))
    text = input("Digite uma data: ") if option == 1 else get_audio()
    print(text)

    CALENDAR_STRS = ["what i do have", "do i have plans", "am i busy", ""]

    for phrase in CALENDAR_STRS:
        if phrase in text.lower():
            date = get_date(text)
            if date:
                service = authenticate_google()
                get_events(date, service)
            else:
                speak('[ERROR]Try again')


if __name__ == "__main__":
    main()
