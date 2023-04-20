#Crie um programa que Leia: Nome, sexo e idade de várias pessoas, guardando cada pessoa em um dicionário
#todos os dicionarios em uma lista
#no final mostre:
'''
A) Quantas pessoas foram cadastradas?
B) A média de idade do grupo
C) uma lista com todas as Mulheres
D) Uma lista com todas as pessoas com idade acima da média
'''

'''cadastro = []
while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: '))

    #Validando se está digitando mM Ff
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] '))
        if pessoa['sexo'] in 'MmFf':
            break
        print('Digite um valor valido: ')

    pessoa['idade'] = int(input('Idade: '))
    cadastro.append(pessoa)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
print('-='*30)

#Fazendo a média e a varredura em cada pessoa['idade']
soma = 0
for pessoa in cadastro:
    soma += pessoa['idade']
media = soma/len(cadastro)

print(f'- O grupo tem {len(cadastro)} pessoas')
print(f'- A média de idade é de {media} anos')

# Varrendo a lista para saber quem é Mulher pela key sexo:
for pessoa in cadastro:
    if pessoa['sexo'] == 'f':
        print(pessoa['nome'], end=' ')

#PULAR LINHA
print()

#VARRENDO A IDADE PARA SABER QUEM É MAIOR QUE A MEDIA
for pessoa in cadastro:
    if pessoa['idade'] > media:
        print(f'nome = {pessoa["nome"]}; sexo = {pessoa["sexo"].upper()}; idade = {pessoa["idade"]}')

print('<< ENCERRADO >>')
'''


#Resolução Guanabara
galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp in 'nN':
        break

print('-'*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas. ')
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos')
print('As mulheres cadastradas foram ', end='')

for pessoa in galera:
    if pessoa['sexo'] in 'Ff':
        print(f'{pessoa["nome"]}', end=' ')

print()
print('D) lista das pessoas que estão acima da média: ', end='')
for pessoa in galera:
    if pessoa['idade'] > media:
        print(f'nome = {pessoa["nome"]}; sexo = {pessoa["sexo"].upper()}; idade = {pessoa["idade"]}')