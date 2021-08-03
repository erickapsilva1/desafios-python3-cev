# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

pproduto = float(input("Informe o preço: "))
desconto = pproduto - (pproduto * 0.05)

print('Valor inicial: {} e com desconto {}'.format(pproduto, desconto))
