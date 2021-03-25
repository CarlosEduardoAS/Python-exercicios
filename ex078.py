valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(f'O maior valor foi {sorted(valores)[-1]} na posição {valores.index(sorted(valores)[-1])}.')
print(f'O menor valor foi {sorted(valores)[0]} na posição {valores.index(sorted(valores)[0])}.')