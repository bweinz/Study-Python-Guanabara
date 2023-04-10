#Desafio 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar:
valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o valor do seu salário? R$'))
anos = int(input('Em quantos anos quer pagar a casa? '))
salario_liquido = ((salario / 100) * 30)
meses = (anos * 12)
prestacao_mensal = round((valor_casa / meses),2)

print('seu salario é de R${}, os 30% do salario é R${}, você escolheu comprar a casa em {} anos, equivalente á {} meses, a prestação da casa é igual à R${}'.format(salario, salario_liquido, anos, meses, prestacao_mensal))

if salario_liquido >= prestacao_mensal:
    print('Empréstimo Concedido')
else:
    print('Emprestimo Negado')

    