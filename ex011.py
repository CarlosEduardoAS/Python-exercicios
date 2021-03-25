l = float(input('Largura da parede(em metros): '))
al = float(input('Altura da parede(em metros): '))
ar = l*al
q = ar/2
print('\033[1;30;44m Área da parede:\033[m \033[1;4;31m{}m²\033[m \n\033[1;30;44m Quantidade de tinta(em litros) necessária para pintar:\033[m \033[1;4;31m{}L\033[m'.format(ar, q))