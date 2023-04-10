#Ex 38: escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
'''
- 0 primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

valor1 = int(input('Digite o primeiro Valor: '))
valor2 = int(input('Digite o segundo Valor: '))

if valor1 > valor2:
    print('O primeiro valor é maior que o segundo')
elif valor2 > valor1:
    print('O segundo valor é maior que o primeiro')
else:
    print('não existe valor maior, os dois são iguais')