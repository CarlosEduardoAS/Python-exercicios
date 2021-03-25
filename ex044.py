p = float(input('Digite o preço do produto: R$'))
cp = int(input('''Digite o número condizente a sua forma de pagamento:
[ 1 ] Dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
'''))
if cp == 1:
    np = p - (p*0.1)
elif cp == 2:
    np = p - (p*0.05)
elif cp == 3:
    np = p
elif cp == 4:
    np = p + (p*0.2)
else:
    np = p
    print('Número inválido. Tente novamente.')
print('O valor a ser pago é de R${}.'.format(np))