# programa que leia 5 núm. inteiros e coloque numa tupla
# depois mostre a listagem dos números gerados e também indique o maior, menor

from random import randint
numeros = (randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99))
print(numeros)
print('Maior:', max(numeros))
print('Menor:', min(numeros))
