op = 's'
q = s = maior = menor = 0
while op in 's':
    num = int(input('Digite um número inteiro: '))
    q += 1
    s += num
    if q == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    op = str(input('Quer continuar (s/n)? ')).lower()
m = s / q
print('A média dos {} valores digitados foi {:.2f}.'.format(q, m))
print('O maior número foi o {} e o menor foi o {}.'.format(maior, menor))