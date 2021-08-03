# Faça um mini-sistema que utilize interactive-help do Python. O usuário vai digitar o comando e o manual
# vai aparecer. Quando o usuário digitar a palavra FIM, o programa vai se encerrar.
# Obs: use cores.

from time import sleep

c = ('\033[m',           # 0 - sem cores
     '\033[0;30;41m',    # 1 - vermelho
     '\033[0;30;42m',    # 2 - verde
     '\033[0;30;43m',    # 3 - amarelo
     '\033[0;30;44m',    # 4 - azul
     '\033[0;30;45m',    # 5 - roxo
     '\033[7;30m',       # 6 - branco
     );


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


# Main
comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.lower() == 'fim':
        break
    else:
        ajuda(comando)
titulo('Até logo :)', 1)

