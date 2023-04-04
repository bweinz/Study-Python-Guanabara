#Ex52: Faça um programa que leia um número inteiro e diga se ele é ou não um número Primo

n1 = int(input('digite um valor: '))
total = 0

for n in range (1, n1+1):

        if n1 % n == 0:
                print('\033[33m', end=' ')
                total += 1
        else:
                print('\033[31m', end=' ')
        print(f'{n}', end=' ')
print(f' \n o numero {n1} foi divisivel {total} vezes')

if total == 2:
        print('Numero Primo')
else:
        print('Numero Não Primo')