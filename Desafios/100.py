# programa que tenha uma lista chamada números
# e duas funcoes chamadas sorteio e somaPar
# a primeira função vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda funcao
# vai mostrar a soma entre todos os valores pares sorteados pela funcao anteior

from random import randint
from time import sleep


def sorteio(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        n = randint(1, 10)
        lst.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO')


def somaPar(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lst}, temos {soma}.')


numeros = list()
sorteio(numeros)
somaPar(numeros)