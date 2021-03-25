from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Há {} pessoas maiores de idade e {} menores de idade.'.format(maior, menor))