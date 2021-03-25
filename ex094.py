pessoa = {}
lista = []
toti = m = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().lower()[0]
        if pessoa['sexo'] in 'mf':
            break
        print('ERRO! por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    toti += pessoa['idade']
    lista.append(pessoa.copy())
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar? ')).lower()[0]
    if op == 'n':
        print('-='*30)
        print(lista)
        print(f'- O grupo tem {len(lista)} pessoas.')
        m = toti / len(lista)
        print(f'- A média de idade é de {m:5.2f} anos.')
        print('- As mulheres cadastradas foram: ', end='')
        for p in lista:
            if p['sexo'] in 'f':
                print(f'{p["nome"]} ', end='/')
        print()
        print('- Lista das pessoas que estão acima da média: ', end='')
        for p in lista:
            if p['idade'] >= m:
                print(' ', end='')
                for k, v in p.items():
                    print(f'{k} = {v}; ', end='')
                print()
        break
print('<< ENCERRADO >>')