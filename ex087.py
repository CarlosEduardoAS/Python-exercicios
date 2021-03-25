matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            sp += matriz[l][c]
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {sp}.')
soma3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é {soma3}.')
print(f'O maior valor da segunda linha é {sorted(matriz[1])[-1]}.')