# Crie um programa que leia um número real qualquer
# pelo teclado e mostre na tela a sua porção inteira

import math
num = float(input("Digite um número: "))
print("O inteiro de {} é {}".format(num,math.ceil(num)))