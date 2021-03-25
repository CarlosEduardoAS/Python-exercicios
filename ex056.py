s = 0
mih = 0
nv = ''
totm20 = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M/F): ')).strip()
    s += idade
    if c == 1 and sexo in 'Mm':
        mih = idade
        nv = nome
    if sexo in 'Mm' and idade > mih:
        mih = idade
        nv = nome
    if sexo in 'Ff' and idade < 20:
        totm20 += 1
m = s/4
print('A média das idades foi {}.'.format(m))
print('O homem mais velho tem {} anos e se chama {}.'.format(mih, nv))
print('Ao todo, são {} mulheres com menos de 20 anos.'.format(totm20))