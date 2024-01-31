from random import randint

numero = int(input('qual número estou pensando entre 0 a 5?'))
numeroDoPc = randint(0, 5)
if numero == numeroDoPc:
    print('voce acertou!!')
else:
    print('não foi dessa vez :(')