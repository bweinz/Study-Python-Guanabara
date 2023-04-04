#65: Crie um programa que leia varios numeros inteiros pelo teclado no final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuario se ele quer continuar ou não

condicao = ' '
n = 0
soma = 0
maior = 0
menor = 0
media = 0
contador = 0
lista = []

while condicao != 'N':
    n = int(input('Digite um valor númerico: '))
    condicao = str(input('Você deseja continuar? [S/N]: ')).upper()
    soma += n
    contador += 1
    lista.append(n)
    menor = min(lista)
    maior = max(lista)
media = soma / contador

print(f'a soma dos valores é igual à {soma} \n a média dos valores é igual á {media} \nO maior número é igual a {maior} \nO menor é igual a {menor} Fim')