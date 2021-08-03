# Programa que simule um jogo com 4 jogadores
# Onde cada jogador joga um dado e o programa faça um ranking

from random import randint
from time import sleep
from operator import itemgetter

# Número aleatório para cada jogador
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
# imprime
print(jogo)

ranking = dict()

# Para cada item, impreme os valores formatados:
print('Valores sorteador: ')
for k, v in jogo.items():
    print(f'{k} tirou o {v} no dado.')
    sleep(1)

# Faz a classificação usando o itemgetter de forma reversa.
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)

for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)