# Faça um algoritmo que leia o ordenado de uma pessoa
# e mostre seu novo salário com 15% de aumento.

ordenado = float(input("Ordenado: "))
aumento = ordenado + (ordenado* 0.15)

print('Ordenado: {}, com aumento de 15% = {}'.format(ordenado, aumento))
