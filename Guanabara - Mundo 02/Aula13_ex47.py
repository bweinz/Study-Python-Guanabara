#Ex 47 Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

for n in range (2, 51, 2): #Começando do 2 pulando de 2 em 2
  if n % 2 == 0:
      print(n, end=' ') #end faz com que fique tudo na mesma linha