# Escreva um programa que faça o PC pensar num número inteiro de 0 a 5 e diga se
# a gente acertou ou não.

from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar num número entre 0 e 5')
print('-=-' * 20)
pc = randint(0, 5)
player = int(input("Em qual número eu estou pensando? "))
print('PROCESSANDO...')
sleep(3)
if player == pc:

    print('Parabéns, você acertou!')
else:
    print('Errou, o número é', pc)