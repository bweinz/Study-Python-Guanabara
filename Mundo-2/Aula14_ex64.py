#Ex 64 Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. no Final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o 999

n = 0
soma = 0
contador = 0
n = int(input('Digite um número qualquer: '))

while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um número qualquer: '))
print("FIm")
print(f' a soma dos valores é igual a {soma} e você digitou {contador} valores')
