def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: o número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            print(c, end='')
            print(' x ' if c > 1 else ' = ', end='')
    return f


print('--'*20)
print(fatorial(5, True))