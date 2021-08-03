# Faça um programa que leia a largura e altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m2

# area = altura * comprimento
altura = float(input("Digite a altura: "))
comprimento = float(input("Digite o comprimento: "))

area = altura * comprimento
tinta = area / 2

print('Área total: {} m2.'.format(area),'\n'
                                     'Litros de tinta necessários: {} '.format(tinta))