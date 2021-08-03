# programa que leia o ano de nascimento e informe:
# se ele ainda vai se alistar
# se é hora de se alistar
# se passou do tempo

import time

alist = int(17)
anoNasci = int(input('Informe seu ano de nascimento: '))
ano = int(time.strftime("%Y"))

test = ano - anoNasci

if test > alist:
    print('Você já passou {} anos do período de alistamento.'.format(test - alist))
elif test < alist:
    print('Você está {} anos adiantado para o alistamento'.format(alist - test))
elif test == alist:
    print('Já é hora para o alistamento!')
