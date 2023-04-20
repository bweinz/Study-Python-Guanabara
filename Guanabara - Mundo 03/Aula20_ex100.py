#Faça um programa que tenha uma lista chamada numeros e duas funcoes chamadas sorteia() e SomaPAr()
#A primeira função vai sortear 5 números e vai colocálos dentro da lista e a segunda funcao vai mostrar a soma entre todos os valores pares sorteados pela função anterior

#Sorteando:
''' Minha Def de Aleatorio:

import random
def sorteia(amount):
    sorteados = []
    for i in range(amount):
        numero_sorteado = random.randint(1,10)
        sorteados.append(numero_sorteado)
    print(sorteados)

sorteia(50)'''


from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('Pronto')

numeros = []
sorteia(numeros)

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


somaPar(numeros)

