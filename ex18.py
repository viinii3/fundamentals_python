from random import choice

nome1 = input('digite um nome:')
nome2 = input('digite outro nome:')
nome3 = input('digite outro nome:')
nome4 = input('digite outro nome:')

nomes = [ nome1, nome2, nome3, nome4]

print('o nome escolhido é do/da {}'.format(choice(nomes)))