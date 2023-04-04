#Ex 48 Faça um programa que calcule a soma entre todos os números impares que são Multiplos de três e que se encontram no intervalo de 1 até 500
soma = 0
cont = 0
for n in range (1, 501, 2):
    if n % 3 == 0:
        soma += n       #soma os valores encontrados
        cont += 1       #soma a quantidade de vezes que acha, cada vez que achar soma +1

print(soma, end=' ')
print(cont, end=' ')