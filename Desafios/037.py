# escolher as opções e converter

num = int(input('Digite um número inteiro: '))
print('''Escolha: 
1 - Binário
2 - Octal
3 - Hexadecimal''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('{} é uma opção inválida! Nenhum conversão será feita.'.format(num))