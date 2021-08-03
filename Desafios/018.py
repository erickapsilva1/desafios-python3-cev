'''
Programa que leia um ângulo qualquer e mostre na tela o valor do ceno,
cosseno e tangente desse ângulo.
'''
import math
angulo = float(input('Valor do ângulo: '))
print('Ceno: {}, Cosseno: {}, Tangente: {}.'.format(math.sin(angulo),math.cos(angulo),math.tan(angulo)))