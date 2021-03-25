def metade(n=0, form=False):
    res = n / 2
    return res if form is False else moeda(res)


def dobro(n=0, form=False):
    res = n * 2
    return res if form is False else moeda(res)


def aumentar(n=0, perc=0, form=False):
    res = n + (n * perc/100)
    return res if form is False else moeda(res)


def diminuir(n=0, perc=0, form=False):
    res = n - (n * perc/100)
    return res if form is False else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

def resumo(n=0, aumenta=0, reduz=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aumenta}% de aumento: \t{aumentar(n, aumenta, True)}')
    print(f'{reduz}% de redução: \t{diminuir(n, reduz, True)}')
    print('-'*30)