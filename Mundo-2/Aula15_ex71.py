'''Crie um programa que simule o funcionamento de um caixa eletronico.
No início pergunte ao usuário qual sera o valor a ser sacado (numero inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues
Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1 '''

'''import math

valor = 0
nota_cinquenta = 0
nota_vinte = 0
nota_dez = 0
nota_um = 0
sobra_cinquenta = 0
sobra_vinte = 0
sobra_dez = 0
sobra_1 = 0
valor = int(input('Que valor você quer sacar? R$ '))

nota_cinquenta = valor / 50
sobra_cinquenta = valor % 50

nota_vinte = sobra_cinquenta / 20
sobra_vinte = sobra_cinquenta % 20

nota_dez = sobra_vinte / 10
sobra_dez = sobra_vinte % 10

nota_um = sobra_dez / 1

print(f'Total de {math.floor(nota_cinquenta)} cédulas de R$50,00, ')
print(f'Total de {math.floor(nota_vinte)} cédulas de R$20,00')
print(f'Total de {math.floor(nota_dez)} cédulas de R$10,00')
print(f'Total de {math.floor(nota_um)} cédulas de R$1,00')'''


valor = int(input('Que valor você quer sacar? R$'))
cedula = 50
total_cedulas = 0
while True:
    if valor >= cedula:                 #Se o valor de saque for maior que a cedula de 50
        valor = valor - cedula          #Valor de saque agora recebe o valor - 50
        total_cedulas += 1              #No loop cada vez que o valor for maior que 50 o total de cedulas aumenta 1
    else:                               #Se não for maior que 50 muda a cedula
        if total_cedulas > 0:           # Se o total de cedula for maior que 0
            print(f'Total {total_cedulas} cédulas de R${cedula}')   #escreva total (quantidade de notas que passou da verificação anterior ou seja, maior que 50), cedular de (valor atual de teste 50)
        if cedula == 50:                   #se o valor atual for igual 50, mude para 20 e refaça o primeiro teste
            cedula = 20
        elif cedula == 20:                  #se o valor atual for igual 20, mude para 10 e refaça o primeiro teste
            cedula = 10
        elif cedula == 10:                  #se o valor atual for igual 10, mude para 1 e refaça o primeiro teste
            cedula = 1
        total_cedulas = 0
        if valor == 0:                      # quando o valor chegar em 0 saia do laço
            break