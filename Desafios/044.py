# programa que calcule o valor a ser pago por um produto, considerando seu preço normal
# e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# até 2x no cartão: preço normal
# 3x ou mais no cartão 20% de juros

fPagamento = int(input('''Formas de pagamento: 
1 - À vista dinheiro
2 - À vista cheque
3 - À vista no cartão
4 - 2 x no cartão
5 - 3 x ou mais no cartão
----> '''))
vProd = float(input('Valor do produto: '))

if fPagamento == 1 or fPagamento == 2:
    print('10% DESC.: ', vProd - (vProd * 0.1))
elif fPagamento == 3:
    print('5% DESC.: ', vProd - (vProd * 0.05))
elif fPagamento == 4:
    print('SEM DESC.: ', vProd)
elif fPagamento == 5:
    print('20% JUROS: ', vProd + (vProd * 0.2))