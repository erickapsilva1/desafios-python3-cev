# programa que leia o peso de 5 pessoas
# No final, mostre qual foi o maior e o menor peso lidos

menorPeso = 0
maiorPeso = 0
for kg in range(1, 6):
    peso = float(input('Informe o {} peso: '.format(kg)))
    if kg == 1:
        menorPeso = peso
        maiorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        elif peso < menorPeso:
            menorPeso = peso

print('Menor peso: ', menorPeso)
print('Maior peso: ', maiorPeso)