# Programa que leia 0 a 9999 e mostre
# na tela cada um dos digitos separados

valor = str(input('Digite um número de 0 a 9999: '))

unidade = ['Milhar: ', 'Centena: ', 'Dezena: ', 'Unidade: ']
j = 0

for i in valor[::1]:
    print(unidade[j] + i)
    j += 1

