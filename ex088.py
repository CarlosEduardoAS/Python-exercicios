from random import randint
from time import sleep
print('---'*10)
print(f'{"JOGUE NA MEGA SENA":^5}')
print('---'*10)
num = int(input('Quantos jogos deseja sortear? '))
if num > 0:
    if num > 1:
        print(f'-=-=-= SORTEANDO {num} JOGOS -=-=-=')
    else:
        print(f'-=-=-= SORTEANDO {num} JOGO -=-=-=')
    for c in range(0, num):
        jogo = []
        for x in range(0, 6):
            n = randint(1, 60)
            if n not in jogo:
                jogo.append(n)
        print(f'Jogo {c+1}: {sorted(jogo)}')
        sleep(1)
        jogo.clear()
    print('-=-=-=-= < BOA SORTE! > -=-=-=-=')