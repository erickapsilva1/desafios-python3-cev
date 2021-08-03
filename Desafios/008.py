# Escreva um programa que leia um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

metros = int(input('Quantos metros? '))
centimetos = metros * 100
milimetros = metros * 1000
print('Ahh, seus {} metros são {} centimetros ou {} milimetros.'.format(metros, centimetos, milimetros))