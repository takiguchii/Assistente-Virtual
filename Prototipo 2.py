#Bibliotecas 
import keyboard
import speech_recognition as sr

r = sr.Recognizer()

#função do reconhecimento de fala 
def listen_command():
    with sr.Microphone() as source:
        print("Aguardando comando...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language='pt-BR')
        print("Comando reconhecido:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o comando. Tente novamente.")
        return ""
    except sr.RequestError as e:
        print("Não foi possível realizar a solicitação; {0}".format(e))
        return ""

#importando lista de comandos 
from command import command_actions

#Função que FAz a chamada da lista de comandos 
def execute_command(command):
    for condition, action in command_actions:
        if condition in command:
            action()
            break
    else:
        print("Comando não reconhecido.")

#Importando funções ja pré programadas 
from audio_options import PrevisãoDoTempo, musica, discord, maps, tradutor, exit_program, greet,chrome

#função principal (main)
def main():
    print("Pressione a tecla (pause) para ativar o reconhecimento de voz.")
    while True:
        if keyboard.is_pressed("pause"):
            command = listen_command()
            if command:
                execute_command(command)
            print("Pressione F1 novamente para realizar outro comando.")
if __name__ == "__main__":
    main()
