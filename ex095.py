jogador = {}
lista = []
while True:
    jogador.clear()
    print('---'*11)
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    np = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    tot = 0
    for c in range(0, np):
        g = (int(input(f'Quantos gols na {c+1}º partida? ')))
        gols.append(g)
        tot += g
    jogador['gols'] = gols
    jogador['total'] = tot
    lista.append(jogador.copy())
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar? [S/N] ')).lower()[0]
    if op == 'n':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('---'*13)
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('---'*13)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f'ERRO! Não existe jogador com códico {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {lista[busca]["nome"]}:')
        for i, g in enumerate(lista[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')