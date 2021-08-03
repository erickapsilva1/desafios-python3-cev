# Programa que tenha uma função chamada área que recebe as dimensoes de um terrono
# retangular (largura e comprimento) e mostre a área do terreno


def area(lar, com):
    a = lar * com
    print(f'A área de um terreno {lar} x {com} é de {a} m2.')


print(' Controle de Terrenos')
print('-' * 20)
lar = float(input('LARGURA (m): '))
com = float(input('COMPRIMENTO (m): '))
area(lar, com)