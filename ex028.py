from random import randint
from time import sleep
nc = randint(0, 5)
print('-=-'*10)
print('Pensei em um número de 0 a 5.')
print('-=-'*10)
nu = int(input('Tente advinhar: '))
print('Processando...')
sleep(2)
if nu == nc:
    print('Parabéns! Você acertou!')
else:
    print('Você errou. A resposta é {}'.format(nc))