from random import randint
c = u = op = r = q = 0
print('=-=-='*4)
print('JOGO DE PAR OU ÍMPAR')
print('=-=-='*4)
while True:
    c = randint(1, 10)
    u = int(input('Digite um valor entre 1 e 10: '))
    op = str(input('Par ou Ímpar? [P/I] ')).strip().lower()[0]
    if (u+c) % 2 == 0:
        r = 'par'
    else:
        r = 'ímpar'
    print('-----'*12)
    print(f'Você jogou {u} e o computador jogou {c}. O total deu {u+c} = {r}')
    if op == 'p' and r == 'par' or op == 'i' and r == 'ímpar':
        print('-----' * 12)
        print('Você ganhou!')
        q += 1
    else:
        print('-----' * 12)
        print('Você perdeu.')
        print('=-=-=' * 5)
        print(f'Número de vitórias: {q}')
        break
