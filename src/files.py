

def create_file(text):
    file = open('Downloads/texto.txt','a')
    file.write(f"{text} \n")
    file.close()


def read_file():
    from src.assistant import speak, googleSpeak

    file = open("Downloads/texto.txt",'r', encoding="utf-8")
    text = file.read()
    print(text)
    print('Generating audio, please wait...')
    googleSpeak(text, 'pt')
    file.close()
