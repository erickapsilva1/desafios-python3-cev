# programa que leia vários n. inteiros, só vai parar com 999
# ao final, tem que mostrar a soma desconsiderando a flag

n = int(input('Digite um número: '))
cont = 0
soma = 0

while n != 999:
    cont += 1
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
print('Saindo...')
print('A soma dos {} valores foi {}: '.format(cont, soma))