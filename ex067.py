n = 0
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    print('===' * 10)
    if n < 0:
        print('PROGRAMA ENCERRADO')
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('===' * 10)