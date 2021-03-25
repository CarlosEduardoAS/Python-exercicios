s = 0
for c in range(1, 7):
    n = int(input('Digite o {}° número inteiro: '.format(c)))
    if n % 2 == 0:
        s += n
print('A soma entre os números pares é {}.'.format(s))