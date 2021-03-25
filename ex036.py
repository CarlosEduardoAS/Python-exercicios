v = float(input('Digite o valor da casa: R$'))
s = float(input('Digite o seu salário: R$'))
a = int(input('Digite em quantos anos o valor será pago: '))
pm = v / (a*12)
if pm > (s*0.3):
    print('Empréstimo NEGADO\nInfelizmente você não poderá financiar esta casa, pois a prestação mensal de R${:.2f} excede os 30% do seu salário.'.format(pm))
else:
    print('Empréstimo CONCEDIDO\nA casa será financiada através de prestações mensais de R${:.2f}.'.format(pm))