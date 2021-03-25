def area(larg, comp):
    a = l * c
    print(f'A área do terreno {l}x{c} é de {a}m².')


# Programa Principal
print('Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)