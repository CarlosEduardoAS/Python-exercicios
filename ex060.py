num = int(input('Digite um número inteiro: '))
c = num
f = 1
print('{}! = '.format(num), end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)


'''for x in range(num+1, 1):
    c -= 1
    f *= c
print(f)'''