#Ex59: Crie um programa que leia dois valores e mostre um menu na tela
'''
1 - Somar
2 - multiplicar
3 - maior
4 - novos números
5 - sair do programa

'''

menu = 0
resultado = 0
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro Valor: '))

while menu != 5:

    menu = int(input('[1] Somar \n'
                     '[2] Multiplicar\n'
                     '[3] Maior\n'
                     '[4] Novos Números\n'
                     '[5] Sair\n'))
    if menu == 1:
        resultado = n1 + n2
        print(f'a soma dos valores é igual á {resultado}')
    elif menu == 2:
        resultado = n1 * n2
        print(f'a multiplicação dos valores é igual á {resultado}')
    elif menu == 3:
        if n1 > n2:
            print(f'o maior número digitado foi: {n1}')
        else:
            print(f'o maior número digitado foi: {n2}')
    elif menu == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro Valor: '))

print('Fim')

