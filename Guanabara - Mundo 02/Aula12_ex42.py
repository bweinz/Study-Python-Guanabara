#ex 42: Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
'''
-Equilatero: todos os lados são iguais
-Isosceles: dois lados iguais
-Escaleno: todos os lados diferentes
'''

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
valor3 = float(input('Digite o terceiro valor: '))
triangulo = None

if (valor1 + valor2) > valor3 and (valor1 + valor3) > valor2 and (valor2 + valor3) > valor1:
    triangulo == True
    print('Pode ser um triangulo')
    if valor1 == valor2 and valor1 == valor3 and valor2 == valor3:
        print('Este é um triangulo Equilátero')
    elif (valor1 == valor2 and valor2 != valor3) or (valor2 == valor3 and valor2 != valor1) or (valor1 == valor3 and valor2 != valor1):
        print("Este é um triangulo Isósceles")
    else:
        print('Este é um Triangulo Escaleno')
else:
    print('não pode ser um triangulo')