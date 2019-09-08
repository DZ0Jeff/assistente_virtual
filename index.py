from src.assistant import speak, play, get_audio
from src.files import create_file, read_file
from src.google_calendar import authenticate_google, get_events


def main():
    service = authenticate_google()
    get_events(10, service)


if __name__ == "__main__":
    main()
