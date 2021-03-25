m = 0
mn = 0
for c in range(1, 6):
    p = float(input('Digite o peso da {}ª pessoa em Kg: '.format(c)))
    if c == 1:
        m = p
        mn = p
    else:
        if p > m:
            m = p
        if p < mn:
            mn = p
print('O maior peso da lista é {}kg, e o menor é {}kg.'.format(m, mn))