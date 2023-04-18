'''pessoas = {'nome': 'Bruno', 'idade': '30', 'sexo': 'M'}
for k, v in pessoas.items():
    print(f'{k} = {v}')
print(pessoas.keys())
print(pessoas.values())
pessoas ['nome'] = 'João'
print(pessoas.keys())
print(pessoas.values())
del pessoas['sexo']
print(pessoas)
pessoas['peso'] = 98.5
print(pessoas)'''

#Dicionario dentro de lista
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])'''

estado = {}
brasil = []
for c in range (0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado'))
    brasil.append(estado.copy())
for estado in brasil:
    for v in estado.values():
        print(v, end=' ')
    print()