# melhorar o game do desafio 28, implementando n tentativas até acertar e informar a quantidade de vezes jogadas

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar num número entre 0 e 10')
print('-=-' * 20)
pc = randint(0, 10)
player = int(input("Em qual número eu estou pensando? "))
cont = 0

while player != pc:
    print('PROCESSANDO...')
    sleep(2)
    player = int(input('Não foi dessa vez, tente novamente: '))
    pc = randint(0, 10)
    cont += 1

print('Parabéns, você acertou! Tentou {} vez(es)! '.format(cont))
