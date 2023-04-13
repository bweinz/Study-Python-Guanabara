#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
#no final mostre a matriz na tela com a formatação correta

'''linha1 = [[], [], []]
linha2 = [[], [], []]
linha3 = [[], [], []]
valor = 0

for c in range (0,3):
    valor = int(input(f'Digite um valor para [0, {c}]: '))
    linha1[c].append(valor)

for c in range (0,3):
    valor = int(input(f'Digite um valor para [1, {c}]: '))
    linha2[c].append(valor)

for c in range (0,3):
    valor = int(input(f'Digite um valor para [2, {c}]: '))
    linha3[c].append(valor)

print(linha1)
print(linha2)
print(linha3)
'''

'''princ = [[], [], [], [], [], [], [], [], []]
valor = 0

for c in range (0, 9):
    for l in range(0, 3):
        valor = int(input(f'Digite um valor para [0, {l}] '))
        princ[l].append(valor)

    for l in range(3, 6):
        valor = int(input(f'Digite um valor para [1, {l}] '))
        princ[l].append(valor)
    for l in range(6, 9):
        valor = int(input(f'Digite um valor para [2, {l}] '))
        princ[l].append(valor)
    break
'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-='*30)
for l in range(0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
