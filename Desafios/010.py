# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dolares ela pode comprar
# Considerar: US$ 1.00 = BRL 3.27

reais = int(input('Quantos R$ vocês tem: '))
dolares = reais / 3.27
print('Você pode comprar {} US$ com {} R$'.format(dolares,reais))