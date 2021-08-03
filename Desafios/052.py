# faça um programa que leia um inteiro e diga se ele é ou não um número primo

num = int(input('Digite o número inteiro: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')

print('')

if tot > 2:
    print('O número {} não é primo, pois foi divisível {} vezes!'.format(num, tot))
else:
    print('O número {} é primo!'.format(num))
