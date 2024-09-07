#Importanto lista dde chamadas para o codigo main 
from audio_options import PrevisãoDoTempo, musica, discord, maps, tradutor, exit_program, greet, chrome

#lista dde chamadas 
command_actions = [
    ("navegador", chrome),
    ("abrir navegador", chrome),
    ("previsão do tempo", PrevisãoDoTempo),
    ("música", musica),
    ("discord", discord),
    ("mapa", maps),
    ("tradutor", tradutor),
    ("encerrar", exit_program),
    ("olá", greet)
]
