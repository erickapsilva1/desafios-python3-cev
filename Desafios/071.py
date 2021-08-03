# caixa de banco que cospe as cédulas para fechar o valor sacado.
# considerando apenas cédulas de 50, 20, 10 e 1

print('=' * 30)
print('{:^30}'.format('Banco CEV'))
print('=' * 30)
valor = int(input('Valor a ser sacado: R$'))
total = valor
ced = 50
totCel = 0
while True:
    if total >= ced:
        total -= ced
        totCel += 1
    else:
        if totCel > 0:
            print(f'Total de {totCel} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCel = 0
        if total == 0:
            break