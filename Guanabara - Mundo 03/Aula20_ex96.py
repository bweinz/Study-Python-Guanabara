#Faça um programa que tenha uma função chamada àrea, que receba as dimensões de um terreno retangular (largura e comprimento e mostre a àrea do Terreno.

print('Controle de terrenos')
print('-'*20)

def area(largura, comprimento):
    resultado = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {resultado}m²')

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)

