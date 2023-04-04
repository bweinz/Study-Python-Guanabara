somaidade = 0
mediaidade = 0
maior_idade_homem = 0
nome_mais_velho = ''
mulheres_ate_20 = 0

for p in range (1, 5):
    print(f'-----{p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres_ate_20 += 1


mediaidade = somaidade / 4
print(f'A média de idade é igual á {mediaidade}')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_mais_velho}')
print(f'Ao todo são {mulheres_ate_20} mulheres no grupo com menos de 20 anos')