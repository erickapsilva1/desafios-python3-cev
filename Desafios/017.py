'''
Programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
'''
import math
x = float(input('Valor de X: '))
y = float(input('Valor de Y: '))
compr = math.hypot(x, y)

print('Comprimento: {}'.format(compr))
