# fazer uma função contador
# que receba 3 parâmetros: inicio, meio, e fim e realize a contagem
# o prorama tem que realizar 3 contagens através da função
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contador(i, f, p):
    print('-=' * 50)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.5)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True) # flush para não ligar o buffer de tela
            sleep(0.3)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            cont -= p
            sleep(0.3)
        print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)