# programa que leia o nome e o preço de vários produtos
# perguntando se o user quer ou não continuar
# a) qual é o total de gasto na compra
# b) quantos produtos custam mais de 1000
# c) qual é o nome do mais barato

total = 0
totMil = 0
menor = 0
cont = 0

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        totMil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' Fim do Programa '))
print('Total: ', total)
print('Produtos acima de R$ 1000: ', totMil)
print('O produto mais barato: ', menor)