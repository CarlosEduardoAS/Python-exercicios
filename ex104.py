def leiaInt(txt):
    num = ''
    while num.isnumeric() is False:
        num = input(txt)
        if num.isnumeric():
            return int(num)
        else:
            print('\033[1;31m ERRO! Digite um número inteiro válido.\033[m')


print('-'*30)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')