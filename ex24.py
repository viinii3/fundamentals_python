distancia = int(input('digite a distancia da sua viagem:'))

if distancia <= 200:
    calculoDaviagem = distancia * 0.50
    print('Você esta prestes a começar uma viagem de {}Km, o preço da sua passagem sera de R${:.2f}'.format(distancia, calculoDaviagem))
else:
    calculoDaViagemDesconto = distancia * 0.45
    print('Você esta prestes a começar uma viagem de {}Km, o preço da sua passagem sera de R${:.2f}'.format(distancia, calculoDaViagemDesconto))