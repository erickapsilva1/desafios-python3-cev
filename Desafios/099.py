# programa que tenha uma função chamada maior
# que recebe vários parâmetros com valores inteiros
# seu programa tem que analisar todos os valores e dizer qual dele é o maior

from time import sleep

def maior(*lst):
    print(f'Analisando os valores passados...',flush=True)
    sleep(0.2)
    for c in lst:
        print(f'{c} ', end='', flush=True)
        sleep(0.3)
    print(f'Foram informados {len(lst)} valores ao todo.')
    print(f'O maior valor informado foi {max(lst)}.')
    print('-=' * 50)


maior(5, 10, 44, 109, 666)
maior(0, 0, 1)
maior(8, 10, 10, 2, 1)