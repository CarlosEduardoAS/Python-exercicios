from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa ''')
    opção = int(input('Digite a sua opção: '))
    if opção == 1:
        s = n1 + n2
        print('O resutado de {} + {} é {}.'.format(n1, n2, s))
    elif opção == 2:
        p = n1 * n2
        print('O resultado de {} x {} é {}.'.format(n1, n2, p))
    elif opção == 3:
        if n1 > n2:
            r = n1
        else:
            r = n2
        print('O maior número é o {}.'.format(r))
    elif opção == 4:
        print('Informe os números:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-='*10)
    sleep(2)
print('Fim do programa')