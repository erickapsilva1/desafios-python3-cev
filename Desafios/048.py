# programa que calcula a soma entre todos os números ímpares que são múltiplos de 3
# e que se encontram entre 1 e 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma dos {} elementos é: {}'.format(cont, soma))