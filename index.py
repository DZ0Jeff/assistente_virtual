from src.assistant import speak, play, get_audio, get_date, googleSpeak
from src.files import create_file, read_file
from src.google_calendar import authenticate_google, get_events


def main():
    print('=' * 40, 'Genesis Virtual Assist', '=' * 40)
    
    service = authenticate_google()
    text = input()
    get_events(get_date(text), service)

if __name__ == "__main__":
    main()
