from random import randint
from time import sleep
números = []


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        números.append(n)
        print(n, end=' ')
        sleep(0.5)


def somaPar():
    s = 0
    for p in números:
        if p % 2 == 0:
            s += p
    print(f'\nSomando os valores pares de {números}, temos {s}.')


sorteia()
somaPar()