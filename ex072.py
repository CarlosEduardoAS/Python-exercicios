extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número de 0 à 20: '))
while num > 20 or num < 0:
    num = int(input('Tente novamente. Digite um número de 0 à 20: '))
print(f'O número {num}, por extenso, é {extenso[num]}.')