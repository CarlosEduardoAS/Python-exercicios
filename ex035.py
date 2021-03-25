r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r2 - r3 < r1 < r2 + r3 and r1 - r3 < r2 < r1 + r3 and r1 - r3 < r3 < r1 + r2:
    print('Elas podem formar um triângulo.')
else:
    print('Elas não podem formar um triângulo.')