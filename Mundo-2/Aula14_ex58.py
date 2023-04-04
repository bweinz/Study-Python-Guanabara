#Ex58: melhore o jogo do desafio 028 onde o computador vai "Pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer.

import random

num_aleatorio = random.randint(0, 10)
num_digitado = 0
contador = 0
print(num_aleatorio)

while num_aleatorio != num_digitado:
    num_digitado = int(input('Digite um numero entre 0 e 10 '))
    contador += 1
    if num_digitado > num_aleatorio:
        print('Tente um numero menor')
    else:
        print('Tente um numero maior')
print(f'Você tentou {contador} vezes antes de acertar o valor {num_aleatorio}')
