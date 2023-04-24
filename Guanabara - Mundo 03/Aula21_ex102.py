#Crie um programa que tenha uma função fatorial() que receba dois parametros: o primeiro que indique o numero a calcular e o outro chamado show
#que sera um valor logico opcional indicando se sera mostrado ou não na tela o processo de calculo do fatorial

def fatorial(n, show=False):
   f = 1
   for c in range(n, 0, -1):
       if show:
            print(c, end='')
            if c > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end='')
       f *= c
   print(f)

fatorial(5, show=True)
