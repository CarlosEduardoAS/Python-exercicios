import math
num = float(input('Digite um número: '))
i = math.floor(num)
print('O número \033[1;4;30m{}\033[m tem a parte inteira \033[1;30m{}\033[m.'.format(num, i))