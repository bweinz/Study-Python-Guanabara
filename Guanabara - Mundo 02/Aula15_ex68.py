#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo:

import random
n = 0
cont = 0
parImpar = ''
computador = random.randint(0,10)
verificacao = 0
ganhador = True

print('=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR ')
print('=-'*10)

while True:

    n = int(input('Digite um valor: '))
    parImpar = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    soma = n + computador
    if soma % 2 == 0:
       verificacao = 'Par'
    else:
       verificacao = 'Impar'
    print(f'Você jogo {n} e o computador jogou {computador}. Total de {soma} deu {verificacao}')
    if soma % 2 == 0 and parImpar == 'P' or soma % 2 == 1 and parImpar == 'I':
        print('Você Venceu \n Vamos jogar novamente... ')
    else:
        print(f'\nVocê Perdeu, até agora Venceu {cont} vezes ')
        break
    cont += 1

'''
from random import randint
v = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ''

    #Verificando se realmente digitou P ou I
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu! ')
            v += 1
        else:
            print('Você perdeu')
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu! ')
            v += 1
        else:
            print('Você perdeu! ')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes')

'''

