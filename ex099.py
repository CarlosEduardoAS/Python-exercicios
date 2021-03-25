from time import sleep


def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    cont = 0
    for c in num:
        print(c, end=' ')
        cont += 1
        sleep(0.5)
    print(f' Foram informados {cont} valores ao todo.')
    print(f'O maior valor foi {sorted(num)[-1]}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
