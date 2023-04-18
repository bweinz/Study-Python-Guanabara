#Faça um programa que ajude um jogador da Mega Sena a Criar Palpites;
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
#Para cada jogo, cadastrando tudo em uma lista composta

import random

'''jogos = []
aleatorio = set()

quant = int(input('Quantos jogos você quer que eu sorteie? '))
for q in range(0, quant):
    while len(aleatorio) < 6:
        aleatorio.add(random.randint(1,60))
    jogos.append(aleatorio)
print(jogos)'''

from random import randint
from time import sleep

lista = []
jogos = []
quant = int(input('Quantos jogos voC~e quer que eu jogue? '))
tot = 1
while tot <= quant :

    cont = 0
    num = randint(1, 60)

    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)