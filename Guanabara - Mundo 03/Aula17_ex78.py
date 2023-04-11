#Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for pos, n in enumerate (range(0,5)):
    lista.append(int(input(f'Digite um valor para a Posição {pos}: ')))   #Usei pós enumerate mas poderia ser só atravez do N
print(f'Você Digitou os valores {lista}')
maior = max(lista)
menor = min(lista)
print(f'O maior valor digitado foi {maior} nas posições ', end='')

for index, valor in enumerate(lista):
    if valor == maior:
        print(f'{index}...', end='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for index, valor in enumerate(lista):
    if valor == menor:
        print(f'{index}...', end='')