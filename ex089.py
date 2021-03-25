ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp == 'n':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*35)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*55)
    opc = int(input('Mostrar as notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')