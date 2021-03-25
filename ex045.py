from random import choice
print('\033[1;30m==='*5)
print('\033[1;34mJOGO DE JOKENPÔ')
print('\033[1;30m===\033[m'*5)
j = int(input('''\033[1mDigite o número da sua jogada:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
'''))
l = ['pedra', 'papel', 'tesoura']
c = choice(l)
if 0 < j < 4:
    if c == 'pedra' and j != 1 or c == 'papel' and j != 2 or c == 'tesoura' and j != 3:
        if c == 'pedra' and j == 3:
            print('Você perdeu. Minha jogada foi {}.'.format(c))
        elif c == 'papel' and j == 1:
            print('Você perdeu. Minha jogada foi {}.'.format(c))
        elif c == 'tesoura' and j == 2:
            print('Você perdeu. Minha jogada foi {}.'.format(c))
        else:
            print('Parabéns, você ganhou! Minha jogada foi {}.'.format(c))
    else:
        print('Empate! Eu também joguei {}.'.format(c))
else:
    print('Número inválido. Tente novamente.')