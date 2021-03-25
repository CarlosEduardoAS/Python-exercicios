n = int(input('Digite um número: '))
print('O sucessor de \033[4;30m{}\033[m é \033[1;33m{}\033[m e o antecessor é \033[1;31m{}\033[m.'.format(n, (n+1), (n-1)))