from src.assistant import speak, play, get_audio, googleSpeak, note, call_note
from src.files import create_file, read_file
from src.google_calendar import calendar


def main():
    print('=' * 40, 'Genesis Virtual Assist', '=' * 40)

    text = get_audio().lower()

    call_note(text)
    calendar(text)


if __name__ == "__main__":
    main()
