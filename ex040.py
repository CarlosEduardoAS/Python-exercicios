n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m < 5:
    print('REPROVADO. A sua média foi {}.'.format(m))
elif 5 < m <= 6.9:
    print('RECUPERAÇÃO. Sua média foi {}.'.format(m))
else:
    print('APROVADO. Sua média foi {}.'.format(m))