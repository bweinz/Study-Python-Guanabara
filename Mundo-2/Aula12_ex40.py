#ex40: crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a media atingida:

'''
-média abaixo de 5.o: Reprovado
-Media entre 5.0 e 6.9: Recuperação
-Média 7.0 ou superior: Aprovado
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = ((nota1 + nota2) / 2)

if media < 5:
    print('Reprovado')
elif media >= 5 and media <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')