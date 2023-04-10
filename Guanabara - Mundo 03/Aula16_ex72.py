#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
#Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso.

numero = ('zero', 'um', 'dois', 'três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')




while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n <= 20 and n >= 0:
      print(f'Você digitou o número {numero[n]}')
      break
    else:
      print('Digite um número valido')
