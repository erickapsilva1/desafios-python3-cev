# programa que pergunte salárioe aplique aumento

sal = float(input('Informe o salário: '))
if sal > 1250.0:
    print('Aumento de 10%: R$', sal * 0.1)
    print('Reajustado para: R$', sal + (sal * 0.1))
else:
    print('Aumento de 15%: R$', sal * 0.15)
    print('Reajustado para: R$', sal + (sal * 0.15))