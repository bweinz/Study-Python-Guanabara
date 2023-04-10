#ex54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores:

menores = []
maiores = []

for n in range (0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    if ano < 2002:
           maiores.append(ano)
    else:
            menores.append(ano)
print(f'Existem {len(menores)} menores de 21 anos e {len(maiores)} maiores de 21 anos')
