#Faça um programa que leia nome e média de um aluno, guardando também a situação em um Dicionário. No final mostre o conteúdo da estrutura na tela

aluno = {}
aluno ['nome'] = str(input('Nome: '))
aluno ['media'] = float(input('Media: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situação"]}')

