num = (int(input('Digite o primeiro valor: ')),
 int(input('Digite o segundo valor:')),
 int(input('Digite o terceiro valor:')),
 int(input('Digite o quarto valor: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vez(es).')
if 3 in num:
    print(f'O valor 3 apareceu na {(num.index(3)) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado em nehuma posição.')
print('Os valores pares foram: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')