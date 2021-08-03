# programa que leia seis núm. inteiros e mostre a soma apenas daqules que forem pares
# se for ímpar, tem que desconsiderar

soma = 0
for c in range(1, 7):
    num = int(input('Número {}: '.format(c)))
    if num % 2 == 0:
        soma = soma + num

print('Soma: ', soma)