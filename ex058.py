from random import randint
nc = randint(0, 10)
print('-=-'*11)
print('Pensei em um número entre 0 e 10.')
print('-=-'*11)
nu = int(input('Tente advinhar: '))
t = 0
while nu != nc:
    if nc > nu:
        nu = int(input('Mais... Tente novamente: '))
    else:
        nu = int(input('Menos... Tente novamente: '))
    t += 1
if t > 1:
    print('Você acertou. Foram necessárias {} tentativas.'.format(t + 1))
elif t == 1:
    print('Você acertou. Foram necessárias apenas 2 tentativas.')
else:
    print('Você acertou de primeira!')