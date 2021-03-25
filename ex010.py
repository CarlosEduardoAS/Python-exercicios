r = float(input('Quantidade de dinheiro em reais: R$'))
d = r/4.99
e = r/5.49
print('\033[1;30;44m R${:.2f} \033[m = \033[1;4;30m US${:.2f} \033[m'.format(r, d))
print('\033[1;30;44m R${:.2f} \033[m = \033[1;4;30m EUR${:.2f} \033[m'.format(r, e))