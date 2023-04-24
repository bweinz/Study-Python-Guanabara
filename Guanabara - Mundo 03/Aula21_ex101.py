#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
#Negado, opcional ou obrigatório nas eleições.

#Minha Solução
import datetime

def ano(num=0):
   ano_atual =  datetime.datetime.now().year
   idade = ano_atual - num
   if idade < 18:
       print(f'Com {idade} anos: Voto Negado!')
   elif idade > 18 and idade < 65:
       print(f'Com {idade} anos: Voto Obrigatorio')
   else:
       print(f'Com {idade} anos: Voto Opcional')

num = int(input('Em que ano você nasceu? '))
ano(num)



#Resposta Guanabara:
'''def voto2(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não Vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional.'
    else:
        return f'Com {idade} anos: Voto Obrigatorio.'

print(voto2(2010))'''