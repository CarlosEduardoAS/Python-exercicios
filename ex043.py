p = float(input('Digite seu peso em Kg: '))
a = float(input('Digite sua altura em metros: '))
imc = p/a**2
print('Seu IMC é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif 18.5 <= imc < 25:
    print('Você está com um peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Vocé está com obesidade.')
else:
    print('Você está com obesidade mórbida.')