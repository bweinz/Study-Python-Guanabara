# Crie um programa que leia o nome e o preço de varios produtos
# O programa deverá perguntar se o usuário vai continuar No final mostre:

'''
a) Qual é o total gasto na compra
B) quantos produtos custam mais de R$ 1000
C) qual é o nome do produto mais barato
'''

''' produto = ''
preco = 0
sim_ou_nao = ''
contador = 0
total = 0
produtos = 0
produto_barato = ''
preco_barato = 0
verificador = 0

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    sim_ou_nao = str(input('Quer continuar? ')).upper().strip()

    total += preco
    contador += 1

    if preco >= 1000:
        produtos += 1

    if sim_ou_nao == 'N':
        break

print(f'O total da compra foi {total} ')
print(f'temos {produtos} custando mais de R$1000.00 ')
print(f'O produto mais barato foi {produto_barato} que custa {preco_barato}')'''

total = 0
totmil = 0
menor = 0
cont = 0
barato = ''

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:           #se for o primeiro produto
        menor = preco       # menor preço passa a ser o preço atual
        barato = produto    # o mais barato passa a ser o produto atual
    else:
        if preco < menor:   # Caso não seja o primeiro produto e novo preço seja menor que o preço colocado anteriormente  troca-se o valor para o mais barato
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? S/N ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{" Fim Do Programa " :-^40}')
print(f'O total da compra foi R${total:.2f} ')
print(f'temos {totmil} custando mais de R$1000.00 ')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')
