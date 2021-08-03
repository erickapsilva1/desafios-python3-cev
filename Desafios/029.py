# escreva um programa que leia a velocidade de um carro,
# se passar de 80km ele será multado, e a multa será
# 7,0 reais por km acima.

vm = int(input('Velocidade do carro: '))
if vm <= 80:
    print('OK!')
else:
    print('Você está:', (vm - 80.0), 'acima do permitido! Portando, pagará: R$', (vm - 80.0) * 7)