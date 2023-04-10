#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
'''
A) quantas pessoas tem mais de 18 anos:
B) quantos homens foram cadastrados:
C) quantas mulheres tem menos de 20 anos:

print('-'*10)
print('CADASTRE UMA PESSOA')
print('-'*10)

'''

contador = 0
idade = 0
pessoas_maiores = 0
homens_cadastrados = 0
mulheres_menores = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('[M/F}: ')).strip().upper()[0]
    sim_ou_nao = ' '
    while sim_ou_nao not in 'SN':
        sim_ou_nao = str(input('Quer continuar? [S/N}: ')).upper().strip()[0]
    if idade >= 18:
        pessoas_maiores += 1
    if  sexo == 'M':
        homens_cadastrados += 1
    if idade < 20 and sexo == 'F':
        mulheres_menores += 1

    if sim_ou_nao == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {pessoas_maiores}')
print(f'Ao todo temos {homens_cadastrados} Homens Cadastrados')
print(f'Temos {mulheres_menores} mulheres com menos de 20')