# programa que leia 2 valores e mostre um menu na tela:
# 1 somar, 2 multiplicar, 3 maior, 4 novos números, 5 sair do programa.
# ele deverá realizar a operação em cada caso

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
op = 0

while op != 5:
    op = int(input('''Escolha: 
    [ 1 ] Somar 
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números 
    [ 5 ] Sair do programa
---> '''))

    if op == 1:
        print('SOMA: {} + {} = {}'.format(num1, num2, num1 + num2))
        exit()
    elif op == 2:
        print('MULTIPLICAÇÃO: {} * {} = {}'.format(num1, num2, num1 * num2))
        exit()
    elif op == 3:
        if num1 > num2:
            print('MAIOR: {}'.format(num1))
        else:
            print('MAIOR: {}'.format(num2))
            exit()
    elif op == 4:
        num1 = int(input('Número 1: '))
        num2 = int(input('Número 2: '))

print('Saindo...')
