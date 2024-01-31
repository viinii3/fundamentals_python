numero = int(input('digite um numero:'))
numeroDivisivel = numero % 2

if numeroDivisivel == 0:
    print('o numero {} é um numero PAR'.format(numero))
else:
    print('o numero {} é um numero IMPAR'.format(numero))