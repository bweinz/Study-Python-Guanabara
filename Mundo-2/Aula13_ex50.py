#Ex 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o

soma = 0
cont = 0

for n in range (0, 6):
    valor = int(input('Digite um valor inteiro: '))
    if valor % 2 == 0:
        soma += valor
        cont += 1
print(f' Você informou {cont} números pares e a soma foi {soma}')