from math import sin, cos, tan, radians
num = float(input('digite um angulo:'))
print('o angulo de {} tem o SENO de {:.2f}'.format(num, sin(radians(num))))
print('o angulo de {} tem o COSSENO de {:.2f}'.format(num, cos(radians(num))))
print('o angulo de {} tem a TANGENTE de {:.2f}'.format(num, tan(radians(num))))