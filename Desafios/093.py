jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, total):
    partidas.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {total} partidas.')
print('-=' * 30)
for c in range(0, total):
    print(f'Na partida {c + 1}, fez {partidas[c]} gols.')
print(f'     =>Foi um total de {sum(partidas)} gols!')