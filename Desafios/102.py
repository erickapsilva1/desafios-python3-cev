# programa que tenha uma função fatorial() que receba dois parâmetros
# o primeiro que indique o número a calcular e o outro chamado show, que será um valor
# lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial


def fatorial(num, exibe=False):
    """
    --> Calcula o fatorial de um número
    :param num: número a ter seu fatorial calculado
    :param exibe: mostra o processo de cálculo
    :return: retorna o fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        if exibe:
            print(c, end='')
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
    print('OK')


print(fatorial(5, True))
print(fatorial(5, False))
help(fatorial)