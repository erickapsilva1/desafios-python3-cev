# programa que aprova empréstimo para a compra de uma casa
# valor da casa, salário da pessoa, e quantos anos a pessoa vai pagar
# calcular o valor por mês e se a pessoa vai poder ou não pagar (30% do salário)

salario = float(input('Informe salário: '))
valorCasa = float(input('Informe valor casa: '))
anos = int(input('Informe quantidade de anos: '))
parcelas = int
valorParcelas = float

parcelas = anos * 12
valorParcelas = valorCasa / parcelas

print('Qtd. de parcelas: ', parcelas)
print('Valor: ', valorParcelas)

if valorParcelas >= salario * 0.3:
    print('Você não pode fazer o financeamento!')
    print('30% salário: ', salario * 0.3)
else:
    print('Financeameto será feito')
    print('30% salário: ', salario * 0.3)