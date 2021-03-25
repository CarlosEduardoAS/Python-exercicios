s = float(input('Digite seu salário: R$'))
if s > 1250:
    ns = s + s*0.1
else:
    ns = s + s*0.15
print('O seu novo salário é de R${:.2f}.'.format(ns))