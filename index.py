from src.assistant import speak, play, get_audio, get_date
from src.files import create_file, read_file
from src.google_calendar import authenticate_google, get_events


def main():
    #text = get_audio().lower()
    text = str(input('Option: ')).lower()
    print(get_date(text))


if __name__ == "__main__":
    main()
