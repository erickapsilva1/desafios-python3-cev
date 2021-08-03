# programa que leia vários números inteiros
# só irá parar quando o usuário digitar 999
# no final mostre quantos números foram digitados
# e a soma entre eles, sem considerar a flag

n1 = int(input('Inteiro: '))
cont = 0
soma = 0

while n1 != 999:
    soma += n1
    n1 = int(input('Inteiro: '))
    cont += 1

print('Quantidade de números digitados {}. Soma {}'.format(cont, soma))