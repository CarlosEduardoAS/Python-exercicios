jogador = {}
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
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {np} partidas.')
p = 0
for x in jogador['gols']:
    p += 1
    print(f'    => Na partida {p}, fez {x} gols.')
print(f'Foi um total de {jogador["total"]} gols.')