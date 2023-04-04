#Ex 45: Crie um jogo de jokenpo
import random

lista_do_jogo = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(lista_do_jogo) #random.choice(lista) escolhe 1 dos objetos da lista.

jogador = str(input('Escolha entre Pedra, Papel e Tesoura: '))
jogador = jogador.capitalize() #Capitalize() deixa apenas a primeira letra da palavra em maiuscula
print(f'O jogador escolheu {jogador} o computador {pc}')

if (jogador == 'Pedra' and pc == 'Pedra') or (jogador == 'Tesoura' and pc == 'Tesoura') or (jogador == 'Papel' and pc == 'Papel'):
    print('Empatou')
elif (jogador == 'Pedra' and pc == 'Tesoura') or (jogador == 'Papel' and pc == 'Pedra') or (jogador == 'Tesoura' and pc == 'Papel'):
    print('Jogador Venceu')
else:
    print('Computador Venceu')



