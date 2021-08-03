# programa que leia vários números inteiros
# só irá parar quando o usuário digitar 'sim' ou  'nao'
# no final mostre a média, maior e menor
# e a soma entre eles, sem considerar a flag


n1 = int(input('Inteiro: '))
maior = 0
menor = 0
cont = 0
soma = 0
resp = 'S'

while resp == 'S':
    if cont == 0:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        elif n1 < menor:
            menor = n1

    soma += n1
    cont += 1
    resp = str(input('Continuar? [S] ou [N]').upper())
    if resp.upper() == 'S':
        n1 = int(input('Inteiro: '))


print('Media: ', soma / cont)
print('Maior: ', maior)
print('Menor: ', menor)