lista = list()
dado = list()
mai = men = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(lista) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    lista.append(dado[:])
    dado.clear()
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if op == 'n':
        break
print('-='*30)
print(lista)
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in lista:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi de {men}Kg. Peso de ', end='')
for p in lista:
    if p[1] == men:
        print(f'{p[0]} ')