s = float(input('Seu salário atual: R$'))
ns = s + (s*0.15)
print('Seu \033[1;4;36mnovo salário\033[m é \033[1;4;36mR${:.2f}\033[m.'.format(ns))