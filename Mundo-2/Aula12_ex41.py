#Ex41 A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
'''
- até 9 anos: Mirim
- até 14 anos: Infantil
- até 19 anos: Junior
- até 20 anos: Sênior
- acima: master

'''
ano = int(input("Digite o seu ano de nascimento: "))
mes = int(input("Digite o seu mês de nascimento: "))


from datetime import datetime

agora = datetime.now()
idade = agora.year - ano - ((agora.month, agora.day) < (mes, 1))

print(idade)

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 20:
    print('Senior')
else:
    print('Master')
