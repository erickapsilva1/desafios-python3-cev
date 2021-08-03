# programa que leia o nome de uma
# cidade e diga se ela começa ou não com
# 'Santo'.

citad = input('Digite o nome da cidade: ')
if (citad.split(' ')[0]) == 'Santo':
    print('A cidade {} começa com a palavra SANTO.'.format(citad))
else:
    print('A cidade {} não começa com a palavra SANTO.'.format(citad))
