#Ex 60: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#exemplo: 5! = 5x4x3x2x1 = 120

'''n = int(input("Digite um número inteiro: "))

 Exemplo 10

fatorial = 1                            #Fatorial = 1
while n > 0:                            #Enquanto n for maior que 0
     fatorial *= n                      #1  = 1 * 10 = 10 >  Fatorial = 10 * 9 = 90 > Fatorial = 90 * 8 = 720
     print(fatorial)
     n -= 1                             #N = 10 - 1  = 9  >   N = 9 - 1 = 8   >   N = 8 - 1 = 7
print("O fatorial é:", fatorial)'''



# Com Modulo: Guanabaris:

''' from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')'''

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
print(f'Calculando {n}! = ', end='')
f = 1

while c > 0:
     print(f'{c}', end= '')
     print(' x ' if c > 1 else ' = ', end='')
     f *= c
     c -= 1
print(f'{f}')

#Fazendo com for:


