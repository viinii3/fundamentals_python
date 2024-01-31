nome = input('digite seu nome completo:')

print('analisando seu nome...')
print('seu nome em maiusculo é {}'.format(nome.upper()))
print('seu nome em minusculo é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome é {} e ele tem letras'.format(nome.find(' ')))
