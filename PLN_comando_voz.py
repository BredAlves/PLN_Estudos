import speech_recognition as sr
import os

def abrir_aplicacao(comando):
    """Abre a aplicação correspondente ao comando."""
    aplicacao_map = {
        "navegador": "Chrome.exe",
        "excel": "Excel.exe",
        "powerpoint": "POWERPNT.exe",
        "edge": "msedge.exe",
        "spotify": "spotify.exe",
    }
    if comando in aplicacao_map:
        try:
            os.system(f"start {aplicacao_map[comando]}")
            print(f"Abrindo {comando}")
        except FileNotFoundError:
            print(f"O programa '{comando}' não foi encontrado.")

def ouvir_microfone():
    """Escuta e reconhece a fala do usuário."""
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga Alguma coisa:")
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio, language="pt-br")
            print(f"Você disse: {frase}")
            abrir_aplicacao(frase.lower())  # Converta para minúsculas para evitar problemas de case sensitivity
        except sr.UnknownValueError:
            print("Não entendi o que você disse. Por favor, tente novamente.")
        except sr.RequestError as e:
            print(f"Houve um problema com a requisição; {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

def sair():
    """Encerra o programa."""
    os.system("exit")

while True:
    if ouvir_microfone():
        sair()