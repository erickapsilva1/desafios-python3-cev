# reescrever a função leia_int do ex. 104, mas tratando erros. crie também uma função leia_float


def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('Entrada de dados interrompida pelo user.')
            return 0
        else:
            return n


def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('Entrada de dados interrompida pelo user.')
            return 0
        else:
            return n


n = leia_int('Digite um número: ')
print(f'Inteiro digitado: {n}')
n = leia_float('Digite um número real: ')
print(f'Real digitado: {n}')