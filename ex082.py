números = []
pares = []
ímpares = []
num = 0
while True:
    num = int(input('Digite um número: '))
    números.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        ímpares.append(num)
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if op == 'n':
        print(f'Lista completa: {números}')
        print(f'Lista de números pares: {pares}')
        print(f'Lista de números ímpares: {ímpares}')
        break