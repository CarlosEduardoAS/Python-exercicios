from math import radians, sin, cos, tan
a = float(input('Digite o valor do ângulo: '))
sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('O seno de {} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(a, sen, cos, tan))