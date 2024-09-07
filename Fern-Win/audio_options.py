#bibliotecas
import os
import time
import webbrowser
import subprocess

#função de animação das palavras 
def animate_text(text):
    os.system('cls')
    for letra in text:
        print(letra, end='', flush=True)
        time.sleep(0.02)
    print()

def greet():
    print("Oiê, como posso ajudar?")
    print("")

#função clima 
CLIMA_URL = "https://www.google.com/search?q=previs%C3%A3o+do+tempo&oq=previs%C3%A3o+do+tempo+&aqs=chrome..69i57j35i39i285j0i433i512j0i512l2j0i131i433i512j0i512j0i131i433i512j0i512l2.7764j1j7&sourceid=chrome&ie=UTF-8&dlnr=1&sei=-s3_Y8TiKu2r1sQPjMmxgA0"
def PrevisãoDoTempo():
    animate_text("Okay, vou verificar o clima!!!")
    webbrowser.open(CLIMA_URL, new=2)

#função de musica  OBS:(SÓ VAI FUNCIONAR SE TIVER O SPOTIFLY INSTALADO ), caso não tenha mude a função para webbrowser
def musica():
    animate_text("Tocando musiquinha :3...")
    subprocess.run(["spotify"])

#função de clima 
LOC_URL = "https://earth.google.com/web/search/Rostov,+Rússia/@-22.07521276,-50.29489539,586.53117238a,6465.73140315d,35y,359.98950995h,0t,0r/data=CigiJgokCSc5nuUn3EhAETbe6kBOD0VAGb6Q3wVrsE1AIRZ5EP-Cu0FA" 
def maps():
    animate_text("abrindo localização...")
    webbrowser.open(LOC_URL, new=2)

#função do discord 
DISCORD_URL = "https://discord.com/channels/770127080138211358/1116698331599605780/threads/1121155624357601280"
def discord():
    animate_text("abrindo discord")
    webbrowser.open(DISCORD_URL, new=2)

#função de finalizar comando 
def exit_program():
    print("Encerrando o programa...")
    exit()

#função tradutor
TRANSLATER_URL = "https://translate.google.com.br/?hl=pt-BR"
def tradutor():
    animate_text("abrindo tradutor")
    webbrowser.open(TRANSLATER_URL, new=2)

#função navegador
NAVEGADOR_URL = "www.google.com"
def chrome():
    animate_text("Abrindo o chrome :3...")
    webbrowser.open(NAVEGADOR_URL, new=2)

print("")
    