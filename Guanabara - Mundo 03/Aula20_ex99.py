#Faça um programa que tenha uma função chamada maior(), que receba varios parametros, com valores inteiros
#Seu programa tem que analisar otdos os valores e dizer qual deles é o maior.

def bigger(*num):
    values = num
    amount = len(values)
    biggerValue = max(values)
    print('-='*30)
    print('Analisando os valores passados...')
    print(f'{values} Foram informados {amount} valores ao todo.')
    print(f'O maior valor informado foi {biggerValue}')
    


bigger(2, 9, 4, 5, 7, 1)
bigger(4,7,0)

