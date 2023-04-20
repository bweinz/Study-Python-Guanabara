#Faça um programa que tenha uma função chamada contador(), que receba três parametros: Inicio, Fim e passo e realize a contagem.
#Seu programa tem que realizar tres contagens através da função criada
'''
A) de 1 até 10 de 1 em 1
B) de 10 até 0 de 2 em 2
c) uma contagem personalizada
'''
import time

def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    #time.sleep(2)


    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            #time.sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            #time.sleep(0.5)
            cont -= p
        print('FIM')



contador(1,10,1)
contador(10,0,2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)


