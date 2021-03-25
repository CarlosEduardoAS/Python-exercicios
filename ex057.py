sexo = str(input('Digite seu sexo (M/F): ')).lower().strip()[0]
while sexo != 'm' and sexo != 'f':
    sexo = str(input('Valor inválido. Digite M ou F: ')).lower().strip[0]
if sexo == 'f':
    print('Sexo feminino registrado com sucesso.')
else:
    print('Sexo masculino registrado com sucesso.')