#Ex 49: Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, so que agora utilizando um laço for:

soma = 0
tabuada = int(input('Digite o numero que quer saber a tabuada: '))

for n in range (1, 11):
    soma += tabuada
    print(f'{tabuada} x {n} = {soma}')
