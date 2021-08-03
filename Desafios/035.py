# programa que leia o comprimento de 3 retas e diga se elas podem ou não formar um triângulo

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Segmentos formam um triângulo')
else:
    print('Segmentos NÃO FORMAM um triângulo')