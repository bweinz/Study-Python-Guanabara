#Faça um programa que tenha uma função chama escreva(), que receba um texto qualquer como parametro e mostre uma mensagem com tamanha adaptavel.

'''
Exemplo
escreva('olá,mundo!')

saida
~~~~~~~~~
Ola Mundo
~~~~~~~~~
'''

def escreva(msg):
    tam = len(msg) + 4
    print('~'* tam)
    print(f'  {msg}')
    print('~'*tam)

#Programa Principal
escreva('Banana')
escreva('Gustavo Guanabara')