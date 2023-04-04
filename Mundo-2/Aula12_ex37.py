#Ex 37: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
'''
-1 para binário
-2 para octal
-3 para hexadecimal
'''

numero = int(input('Digite um número inteiro: '))
conversao = int(input('Digite 1 para converter em binário. \nDigite 2 para converter para octal. \nDigite 3 para converter para hexadecimal. \nDigite aqui:  '))
print('o numero escolhido foi {} e sera convertido para: {}'.format(numero, conversao))

if conversao == 1:
    binario = bin(numero) [2:] #fatiando, pulando as 2 primeiras letras que apareciam antes
    print(binario)
elif conversao == 2:
    octal = oct(numero) [2:]
    print(octal)
elif conversao == 3:
    hexadecimal = hex(numero) [2:]
    print(hexadecimal)
else:
    print('Opção invalida')