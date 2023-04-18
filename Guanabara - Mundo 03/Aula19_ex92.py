#Crie um programa que leia nome, ano de nascimento e carteira de trabalho
#cadastre-os (com idade) em um dicionario se por acaso a CTPS
#for diferente de zero, o dicionario recebera também o ano de contratação e o salário.
#calculee acrescente além da idade, com quantos anos a pessoa vai se aposentar 35 anos de trabalho


''' Minha resolução:
dicionario = {}

dicionario['nome'] = str(input('Nome: '))
dicionario['idade'] = 2023 - int(input('Ano de Nascimento: '))
dicionario['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dicionario['ctps'] != 0:
    dicionario['contrataçao'] = int(input('Ano de Contratação: '))
    dicionario['salario'] = float(input('Salário: R$ '))

print(dicionario)

print(f'nome tem o valor de {dicionario["nome"]}')
print(f'idade tem o valor de {dicionario["idade"]}')
print(f'ctps tem o valor de {dicionario["ctps"]}')
if dicionario['ctps'] != 0:
    print(f'Contratação tem o valor {dicionario["contrataçao"]} ')
    print(f'salário tem o valor {dicionario["salario"]}')
    if dicionario["contrataçao"] - 2023 < 35:
        dicionario['aposentadoria'] = (dicionario["idade"] + (dicionario["contrataçao"] - 2023)) + dicionario["idade"]
        print(f'Aposentadorio tem o valor de {dicionario["aposentadoria"]}')
'''
from datetime import datetime


dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contrataçao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrataçao'] + 35) - datetime.now().year)
print(dados)

for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
