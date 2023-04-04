#Ex 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
'''
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
'''
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

mes = int(input('Qual o mes do seu nascimento: '))
ano = int(input('Qual o ano do seu nascimento: '))

agora = datetime.now()
idade = agora.year - ano - ((agora.month, agora.day) < (mes, 1))   #Compara se agora.month(março) < mes(digitado) e se o agora.day(dia atual) é menor que 1

if agora.month < mes or (agora.month == mes and agora.day < 1): #Se o mês atual(03 for menor que o seu mês 07) ou ( 03 for igual a 07 e dia for menor que 1)
    meses = agora.month + (12 - mes) - 1
else:
    meses = agora.month - mes

print(f"Você tem {idade} anos e {meses} meses de idade.")

if idade < 17:
    idade_necessaria = 17 - idade
    print(f"você logo deverá se alistas faltam {idade_necessaria} anos para isso")
elif idade == 17:
    print("Você precisa se alistar.")
else:
    print(f"Você está com suas obrigações atrasadas á {idade-17} anos e {mes} meses")