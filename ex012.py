p = float(input('Preço do produto: R$'))
np = p - (p*0.05)
print('O \033[1;4;30mnovo preço\033[m(5% de desconto) é \033[1;4;30mR${:.2f}\033[m.'.format(np))