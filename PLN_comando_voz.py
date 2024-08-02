print("testando...")


import speech_recognition as sr
import os

#função para ouvir e reconhecer a fala
def ouvir_microfone():

#habilita o microfone do usuario
    microfone = sr.Recognizer()

#usando o microfone
    with sr.Microphone() as source:

        #chama umlgoritmo d recução de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        #frase para o usuario dizer algo
        input("Diga Alguma coisa: ")

        #armazena o que foi dito numa variavel
        audio = microfone.listen(source)

    try:
        #passa a variavel para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language="pt-br")

        if "navegador" in frase:
            os.system("start Chrome.exe")
            return False
        
        elif "Excel" in frase:
            os.system("start Excel.exe")
            return False

        elif "PowerPoint" in frase:
            os.system("start POWERPNT.exe")
            return False   

        elif "Edge" in frase:
            os.system("start msedge.exe")
            return False     

        elif "Sair" in frase:
            os.system("exit")   
            return True
        
        #retorna a frase pronunciada

        print("você disse: " + frase)

        #se não reconheceu o padrao de fala, exibe a mensagem

    except sr.UnknownValueError:
        print("Não entendi")

    return frase

while True:
    if ouvir_microfone():
        break