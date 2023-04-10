#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
#depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

import random

tupla = tuple(random.randint(0, 10) for i in range(5))
print(tupla)
print(f'O maior número gerado foi {max(tupla)}')
print(f'O menor número gerado foi {min(tupla)}')


''' Solução do Guanabara

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

for n in numeros:
    print(f'...max(numeros)
    print(f'...min(numeros)
'''
