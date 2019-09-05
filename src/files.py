

def create_file():
    user = input('Texto aqui: ')
    
    file = open('Downloads/texto.txt','a')
    file.write(f"{user} \n")
    file.close()


def read_file():
    file = open("Downloads/texto.txt",'r', encoding="utf-8")
    text = file.read()
    print(text)
    #print('Generating audio, please wait...')
    #speak(text)
    file.close()