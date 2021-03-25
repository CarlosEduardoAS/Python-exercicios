números = []
num = 0
while True:
    num = int(input('Digite um número: '))
    números.append(num)
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar: [S/N] ')).lower().strip()[0]
    if op == 'n':
        print('-='*20)
        print(f'Foram digitados {len(números)} números.')
        números.sort(reverse=True)
        print(f'A lista em ordem decrescente é: {números}')
        if 5 in números:
            print('O número 5 está na lista.')
        else:
            print('O número 5 não está na lista.')
        break