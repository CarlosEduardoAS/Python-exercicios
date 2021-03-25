num = int(input('Digite um número inteiro qualquer: '))
bc = int(input('''Escolha a base de conversão:
\033[1;30;44m[ 1 ] para BINÁRIO \033[m
\033[1;30;45m[ 2 ] para OCTAL \033[m
\033[1;30;43m[ 3 ] para HEXADECIMAL \033[m
Sua opção: '''))
if bc == 1:
    print('{} = \033[1;34m{}\033[m em \033[1;34mBINÁRIO\033[m'.format(num, bin(num)[2:]))
elif bc == 2:
    print('{} = \033[1;35m{}\033[m em \033[1;35mOCTAL\033[m'.format(num, oct(num)[2:]))
elif bc == 3:
    print('{} = \033[1;33m{}\033[m em \033[1;33mHEXADECIMAL\033[m'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
