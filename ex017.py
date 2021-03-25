import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do  cateto adjacente: '))
h = math.hypot(co, ca)
print('A hipotenusa é \033[1;4;31m{}\033[m.'.format(h))