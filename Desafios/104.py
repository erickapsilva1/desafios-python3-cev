# programa com uma função leiaint()
# que vai funcionar semelhante a input()
# só que fazendo a validação para aceitar apenas um valor numérico
# ex: n = leiaInt('Digite um n')


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Voce acabou de digitar o número: {n}')