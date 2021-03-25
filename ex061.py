print('==='*10)
print('Crie uma progressão aritmética')
print('==='*10)
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
ut = 0
print(pt, end='/')
while ut < 9:
    ut += 1
    pt += r
    print(pt, end='/')
