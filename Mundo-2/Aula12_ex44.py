#ex 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
'''
- A vista dinheiro ou cheque: 10% de desconto
- A vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de Juros
'''

valor_produto = float(input('Digite o Valor do Produto: '))
pagamento = int(input('Escolha uma opção de pagamento:\n'
                      '1 - A vista no dinheiro ou cheque.\n'
                      '2 - A vista no cartão\n'
                      '3 - Em até 2x no cartão\n'
                      '4 - 3x ou mais no cartão\n'
                      'Qual opção deseja escolher?: '
                      ))

print(valor_produto, pagamento)

if pagamento == 1:
    valor_produto = valor_produto - ((valor_produto / 100) * 10)
    print(f'O valor do produto é igual á {valor_produto:.2f}')
elif pagamento == 2:
    valor_produto = valor_produto - ((valor_produto / 100) * 5)
    print(f'O valor do produto é igual à {valor_produto:.2f}')
elif pagamento == 3:
    parcelamento2 = valor_produto / 2
    print(f'O valor do produto é{valor_produto:.2f}, serão duas parcelas de {parcelamento2:.2f}')
elif pagamento == 4:
    valor_produto = valor_produto + ((valor_produto / 100) * 20)
    parcelamento3 = valor_produto / 3
    print(f'O valor do produto ficou em R${valor_produto:.2f} serão três parcelas de {parcelamento3:.2f}')
else:
    print('Valor digitado invalido')
