def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido.')
            continue
        else:
            return n


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro dogitado foi {inteiro} e o real foi {real}')