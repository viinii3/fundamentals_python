numero = float(input('digite um numero em metros para a conversão'))
print('a mediada de {}m corresponde a {}km {}hm {}dam {}dm {}cm {}mm'.format(numero, (numero/1000), (numero/100), (numero/10), (numero* 0.1), (numero*0.01), (numero*0.001)))
