n = int(input('Digite um número diferente de 999: '))
s = n
d = 0
while n != 999:
    n = int(input('Digite mais um número (999 para parar): '))
    s += n
    d += 1
print('A soma dos {} números digitados foi {}.'.format(d, (s - 999)))