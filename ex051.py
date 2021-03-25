print('==='*10)
print('Crie uma progressão aritmética')
print('==='*10)
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
ut = (pt + (10 - 1)*r) + r
for c in range(pt, ut, +r):
    print(c, end='/')