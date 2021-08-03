# programa que jogue jokenpô

import random

opcao = int(input('''Escolha:
--- 1. Pedra
--- 2. Papel
--- 3. Tesoura
--->'''))

sorteio = int(random.randrange(1, 3))

if opcao == 1:
    escolha = 'Pedra'
elif opcao == 2:
    escolha = 'Papel'
elif opcao == 3:
    escolha = 'Tesoura'

if sorteio == 1:
    escolha2 = 'Pedra'
elif sorteio == 2:
    escolha2 = 'Papel'
elif sorteio == 3:
    escolha2 = 'Tesoura'

print('_____________________')
print('     JOKENPÔ!!!!')
print('')
print('JOGADOR: ', escolha)
print('PC: ', escolha2)
print('_____________________')
print('')

if sorteio == 1 and opcao == 1 or sorteio == 2 and opcao == 2 or sorteio == 3 and opcao == 3:
    print('EMPATE!, pois {} é igual a {}'.format(escolha, escolha2))
elif opcao == 1 and sorteio == 3:
    print('Jogador VENCEU, pois {} ganha de {}'.format(escolha, escolha2))
elif opcao == 2 and sorteio == 1:
    print('Jogador VENCEU, pois {} ganha de {}'.format(escolha, escolha2))
elif opcao == 3 and sorteio == 2:
    print('Jogador VENCEU, pois {} ganha de {}'.format(escolha, escolha2))
elif opcao == 1 and sorteio == 2:
    print('PC VENCEU, pois {} ganha de {}'.format(escolha2, escolha))
elif opcao == 2 and sorteio == 1:
    print('PC VENCEU, pois {} ganha de {}'.format(escolha2, escolha))
elif opcao == 3 and sorteio == 1:
    print('PC VENCEU, pois {} ganha de {}'.format(escolha2, escolha))


