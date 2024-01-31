#aprendendo a usar o comando import e from/import

# import math (serve p importat a biblioteca inteira)
# from math import sqrt (serve p importat apenas um item da biblioteca)

from math import sqrt, ceil
num = int(input('digite um numero:'))
raiz = sqrt(num)
print('a raiz de {} é {}'.format(num, ceil(raiz)))

# apenas uma atividade que veio na cabeça de fazer logo abaixo:

from random import randint
numeroChutado = int(input('guess the number:'))
numero = randint(1, 20)

if numero == numeroChutado:
    print('parabens vc acertou o numero')
else:
    print('vishh errou em, o numero era {}'.format(numero))

