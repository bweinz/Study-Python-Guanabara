#Aprimore o exercicio anterior mostrando no final:
'''
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior valor da segunda Linha
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for linha in range(0, 3):                               #Criando 3 linhas
    for coluna in range(0, 3):                          #Criando 3 Colunas
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))   #Input dos valores da linha que serão convertidos em coluna

print('-='*30)
for l in range(0, 3):                                   #para linha de 0 a 2
    for c in range (0, 3):                                  #para coluna de 0 a 2
        print(f'[{matriz[l][c]}]', end='')                  #print a Matriz [[],...] cada valor de Linha em posições 0 0 0 1 0 2 1 0 1 1 1 2
        if matriz[l][c] % 2 == 0:                           #Se o valor digitado na posição da matriz for par
            spar += matriz[l][c]                            #Variavel Soma par recebe spar + o valor digitado
    print()

print(f'A soma dos valores pares é {spar}')

for l in range (0,3):                            #Como já sabemos que a coluna não varia, pois queremos ela usamos a linha para percorer ou seja, a terceira coluna = 0 2, 1 2, 2 2.
    scol += matriz[l][2]                         #soma coluna recebe a scol + o valor da matriz na posição da linha correndo l(0,1,2) e na posição da coluna 2

print(f'A soma dos valores da terceira coluna é {scol}')

for c in range (0,3):                           #Mesma coisa que acima, como temos a linha e queremos saber a coluna, linha 1, varrer colunas 1 0, 1 1, 1 2
    if c == 0:                                  #Se estiver na primeira posição da coluna
        mai = matriz[1][c]                      #Maior = o primeiro valor digitado por estar na primeira iteração do loop
    else:
        if matriz[1][c] > mai:                  #Se não for o primeiro loop e o valor da matriz[na linha 1] [posição do loop atual] for maior que o numero atribuido a maior
            mai = matriz[1][c]                  #Maior passa a ser o novo valor.
print(f'O maior valor da segunda linha é {mai}')