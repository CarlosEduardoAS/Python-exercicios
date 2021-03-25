lista = [[], []]
valor = 0
for n in range(0, 7):
    valor = int(input(f'Digite o {n+1}º número: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-='*30)
print(f'Pares: {sorted(lista[0])}')
print(f'Ímpares: {sorted(lista[1])}')