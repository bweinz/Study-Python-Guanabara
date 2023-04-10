#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do cameponato brasileiro de futebol
#Na ordem de colocação. depois mostre:
'''
A) Apenas os 5 primeiros colocados:
B) os ultimos 4 colocados da tabela:
c) uma lista com os times em ordem alfabética
D) em que posição na tabela está o time da chapecoense
'''

lista = ('América', 'Atletico', 'AtleticoMG', 'Bahia', 'Botafogo', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Cuiaba', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Gremio', 'Internacional', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo', 'Vasco da Gama')

print(f'A lista de times do Brasileirão: {lista}')
print('-='*40)
print(f'Os 5 primeiros são: {lista[0:5]}')
print('-='*40)
print(f'Os 4 ultimos são:{lista[-4: ]}')
print('-='*40)
print(f'Times em ordem alfabética: {sorted(lista)}')
print(f'O Gremio está na {lista.index("Gremio")+1}ª Posição')