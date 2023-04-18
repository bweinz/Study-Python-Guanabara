#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.
#Guarde esses resultados em um dicionario.
#Coloque em ordem sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1,6),
        'jogador2' : randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)
        }
ranking = []
print('Valores Sorteados:')

for key, valor in jogo.items():
    print(f'{key} tirou {valor} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)

for indice, valor in enumerate(ranking):
    print(f'{indice+1} Lugar: {valor[0]} com {valor[1]} Pontos.')