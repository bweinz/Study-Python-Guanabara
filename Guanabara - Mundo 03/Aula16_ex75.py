#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

'''
A) Quantas vezes apareceu o valor 9?
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

n1 = int(input('Digite um número: '))
n2 = int(input('Outro numero: '))
n3 = int(input('mais um número: '))
n4 = int(input('Ultimo: '))
pares = 0
impar = 0

tup1 = (n1, n2, n3, n4)
for n in tup1:
   if n % 2 == 0:
     pares += 1
   elif n % 2 == 1:
     impar += 1


print(f'Você digitou os valores: {tup1}')
print(f'O valor 9 apareceu {tup1.count(9)} vezes')

if 3 not in tup1:
    print('O valor 3 não foi gitiado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {tup1.index(3)+1}º Posição')


print(f'Os valores pares digitados foram {pares}')
