# programa que leia o primeiro termo e a razão de uma PA.
# no final mostre os 10 primeiros termos dessa progressão.

pt = int(input('Informe o 1º termo: '))
rz = int(input('Informe a razão: '))
decTermo = pt + (10 - 1) * rz

for i in range(pt, decTermo, rz):
    print('{} '.format(i), end=' →')
print('FIM')