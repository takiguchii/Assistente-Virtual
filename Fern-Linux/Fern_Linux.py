
# Bibliotecas
import speech_recognition as sr

r = sr.Recognizer()

# Função do reconhecimento de fala
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
        print(f"Não foi possível realizar a solicitação; {e}")
        return ""

# Importando lista de comandos
from command import command_actions

# Função que faz a chamada da lista de comandos
def execute_command(command):
    for condition, action in command_actions:
        if condition in command:
            action()
            break
    else:
        print("Comando não reconhecido.")

# Importando funções já pré-programadas
from audio_options import PrevisãoDoTempo, musica, discord, maps, tradutor, exit_program, greet, chrome

# Função principal (main)
def main():
    print("Ativação concluída, estou ouvindo")

    while True:
        command = listen_command()

        if "reiniciar" in command:
            print("Reiniciando a assistente...")
            break  # Saia do loop para reiniciar

        if command:
            execute_command(command)

        # Opcional: saída do loop ao dizer "sair"
        if "sair" in command:
            print("Encerrando o programa.")
            return  # Encerra o programa

if __name__ == "__main__":
    while True:
        main()
