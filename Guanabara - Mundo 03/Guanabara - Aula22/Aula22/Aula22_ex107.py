#Crie um módulo chamado moeda.py que tenha as funções incorporadas.
#Aumentar, diminuir, Dobro e Metade
#Faça também um programa que importe esse módulo e use algumas dessas funções


from ex107 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p,13)}')