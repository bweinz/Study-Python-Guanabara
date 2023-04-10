#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

n = 0
cont = 1
negativo = '-'
while True:
    n = int(input('Quer ver a tabuada de qual Valor? '))
    cont = 1
    if n < 0:
        break
    while cont < 11:
        m = n * cont
        print(f'{n} x {cont} = {m}')
        cont += 1


