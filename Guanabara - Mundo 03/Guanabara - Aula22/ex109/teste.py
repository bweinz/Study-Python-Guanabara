#Modifique as funções criadas do 107, para que aceitem um parametro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda() desenvolvida no 108

import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p,13, True)}')