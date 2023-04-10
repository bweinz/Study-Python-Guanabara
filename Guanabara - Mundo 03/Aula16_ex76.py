# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequencia:
# no final mostre uma listagem de precos organizados os dados em forma tabular

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')      #:^40 centralizado com 40 espaços
print('-' * 40)

for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end='')    #:.<30 com 30 pontos finais para esquerda
    else:
        print(f'R${listagem[posicao]:>7.2f}')         #:>7.2f Com 7 espaços da direita para esquerda contando 2 casas decimais.