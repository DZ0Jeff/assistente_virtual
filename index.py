from src.assistant import speak, play
from src.files import create_file, read_file
from src.google_calendar import authenticate_google, get_events

def main():
    service = authenticate_google()
    get_events(2, service)


if __name__ == "__main__":
    main()