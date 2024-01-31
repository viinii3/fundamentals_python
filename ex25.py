numero = int(input('digite um numero:'))
numero2 = int(input('digite outro numero:'))
numero3 = int(input('digite outro numero:'))
#verificando o menor
if numero<numero2 and numero<numero3:
    menor = numero
if numero2<numero and numero2<numero3:
    menor = numero2
if numero3<numero and numero3<numero2:
    menor = numero3
print('o menor valor é {}'.format(menor))
#verificando o maior
if numero>numero2 and numero>numero3:
    maior = numero
if numero2>numero and numero2>numero3:
    maior = numero2
if numero3>numero and numero3>numero2:
    maior = numero3
print('o maior valor é {}'.format(maior))