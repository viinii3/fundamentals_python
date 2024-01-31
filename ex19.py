from random import shuffle

nome1 = input('digite um nome:')
nome2 = input('digite um nome:')
nome3 = input('digite um nome:')
nome4 = input('digite um nome:')

nomes = [nome1, nome2, nome3, nome4]
shuffle(nomes)
print('a ordem escolhida foi {}'.format(nomes))