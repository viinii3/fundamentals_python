
from math import hypot
co = float(input('qual o valor do cateto oposto:'))
ca = float(input('qual o valor do cateto adjacente:'))
h1 = hypot(co, ca)
print('o valor da hipotenusa é {:.2f}'.format(h1))