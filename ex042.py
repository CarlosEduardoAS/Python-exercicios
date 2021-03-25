r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        t = 'equilátero'
    elif r1 != r2 != r3 != r1:
        t = 'escaleno'
    else:
        t = 'isóceles'
    print('Elas podem formar um triângulo {}.'.format(t))
else:
    print('Elas não podem formar um triângulo.')