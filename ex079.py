valores = []
op = 0
while True:
    num = (int(input('Digite um valor: ')))
    if num in valores:
        print('Valor duplicado. Não adicionado.')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso...')
        op = ' '
        while op not in 'sn':
            op = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
        if op == 'n':
            print('-='*20)
            print(f'Você digitou os valores {sorted(valores)}')
            break