v = float(input('Digite a velocidade do seu carro agora (em km/h): '))
m = (v - 80) * 7
if v <= 80:
    print('Você está dentro do limite de velocidade.')
else:
    print('Você excedeu o limite de velocidade. Sua multa é de R${:.2f}.'.format(m))