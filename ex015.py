d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
t = (d * 60) + (km * 0.15)
print('O total a pagar é de \033[1;4;31mR${:.2f}\033[m.'.format(t))