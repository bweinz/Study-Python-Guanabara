#ex63 Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} -> {t2}', end='')

contador = 3
while contador <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' -> FIM ')

'''
0 - 1 - 1 - 2 - 3 - 5
        t1  t2  t3
0 - 1 - 1 - 2 - 3 - 5
            t1  t2  t3
0 - 1 - 1 - 2 - 3 - 5 - 8
                t1  t2  t3'''