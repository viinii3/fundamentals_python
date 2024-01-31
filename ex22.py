velocidadeMedia = 80


velocidadeAtual = int(input('digite sua velocidade:'))
if velocidadeAtual <= velocidadeMedia:
    print('esta tudo limpo, boa viagem')
else:
    multa = (velocidadeAtual-80) * 7
    print('você passou do limite da via e por isso vc foi multado; Você deve pagar R${}'.format(multa))