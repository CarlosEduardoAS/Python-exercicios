n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n **(1/2)
cores = {'limpo': '\033[m',
         'número': '\033[1;30m',
         'dobro': '\033[4;34m',
         'triplo': '\033[4;31m',
         'raiz': '\033[4;35m'}
print('O dobro de {}{}{} é {}{}{}, o triplo é {}{}{} e a raiz quadrada é {}{}{}.'.format(cores['número'], n, cores['limpo'], cores['dobro'], d, cores['limpo'], cores['triplo'], t,cores['limpo'], cores['raiz'], r, cores['limpo']))