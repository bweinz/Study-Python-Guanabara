#Crie um pacote chamado utilidadesCeV que tenha dois modulos internos chamados moeda e dado, transfira todas as funções utilizadas nos desafios 107 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from utilidadescev import moeda, dado

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 35,22)