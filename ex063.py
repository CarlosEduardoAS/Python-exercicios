n = int(input('Digite um número inteiro: '))
ut = 2
t1 = 0
t2 = 1
if n >= 2:
    print('{}/{}/'.format(t1, t2), end='')
    while ut < n:
        ut += 1
        t3 = t1 + t2
        print('{}/'.format(t3), end='')
        t1 = t2
        t2 = t3
else:
    print('0')