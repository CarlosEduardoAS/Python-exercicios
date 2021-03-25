nome = preço = caro = barato  = op = tot = menor = c = 0
while True:
    nome = str(input('Nome do produto: ')).strip().lower()
    preço = float(input('Preço: R$'))
    c += 1
    if preço > 1000:
        caro += 1
    if c == 1 or preço < menor:
        menor = preço
        barato = nome
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    if op == 's':
        tot += preço
    else:
        tot += preço
        print(f'O total da compra foi R${tot}')
        print(f'Temos {caro} produtos custando mais de R$1000.00.')
        print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
        break