#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final tudo isso será guardado em um dicionário
#incluindo o total de gols feitos durante o campeonato


dicionario = {}
gols = []

dicionario['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dicionario["nome"]} jogou?: '))

for partida in range (0, partidas):
    gol = int(input(f'Quantos gols na partida {partida}? '))
    gols.append(gol)

dicionario['gols'] = gols[:]
dicionario['total'] = sum(gols)

print('-=' *30)
print(dicionario)
print('-=' *30)

for k, v in dicionario.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' *30)
print(f'O jogador {dicionario["nome"]} jogou {partidas} partidas')
for posicao,valor_gols in enumerate(gols):
    print(f'=> Na Partida {posicao}, fez {valor_gols} Gols ')
print(f'Foi um total de {dicionario["total"]} gols')

