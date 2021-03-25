v = int(input('Digite a distância da sua viagem em Km: '))
if v <= 200:
    p = v * 0.5
else:
    p = v * 0.45
print('A sua viagem custará R${:.2f}'.format(p))