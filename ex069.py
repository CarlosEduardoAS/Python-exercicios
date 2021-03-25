n = idade = m = sexo = h = mmenor = op = 0
while True:
    print('-----' * 5)
    print('CADASTRE UMA PESSOA')
    print('-----' * 5)
    n += 1
    idade = int(input(f'Digite a idade da {n}ª pessoa: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Digite o sexo da pessoa: [M/F] ')).strip().lower()[0]
    if idade >= 18:
        m += 1
    if sexo == 'm':
        h += 1
    if sexo == 'f' and idade < 20:
        mmenor += 1
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if op == 'n':
        print(f'Total de pessoas com mais de 18 anos: {m}')
        print(f'Número de homens cadastrados: {h}')
        print(f'Número de mulheres com menos de 20 anos: {mmenor}')
        break
