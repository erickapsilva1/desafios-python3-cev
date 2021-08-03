# escrever um programa que leia 2 números inteiros e compare-os.
# ver qual é maior, ou se os dois são iguais

num1 = int(input('1º número: '))
num2 = int(input('2º número: '))

if num1 > num2:
    print('Primeiro valor é maior! {}'.format(num1))
elif num2 > num1:
    print('Segundo número é maior! {}'.format(num2))
elif num1 == num2:
    print('Não exite valor maior! Pois {} é = a {}'.format(num1, num2))
else:
    print('Algo deu errado...')