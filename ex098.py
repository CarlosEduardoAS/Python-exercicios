from time import sleep


def contador(i, f, p):
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if p < 0:
        p += -1
    if p == 0:
        p = 1
    if f > i:
        for c in range(i, f+1, p):
            sleep(0.5)
            print(c, end=' ')
        print()
    else:
        for c in range(i, f-1, -p):
            sleep(0.5)
            print(c, end=' ')
        print()


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)