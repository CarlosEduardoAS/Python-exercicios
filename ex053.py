frase = str(input('Digite uma frase: ')).lower().split()[0:]
frase2 = ''.join(frase)
if frase2 == (frase2[::-1]):
    print('Esta frase é um palíndromo.')
else:
    print('Esta frase não é um palíndromo.')