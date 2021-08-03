def aumentar(preco, taxa, format=False):
    res = preco + (preco * taxa) / 100
    return res if format is False else moeda(res)


def diminuir(preco, taxa, format=False):
    res = preco - (preco * taxa) / 100
    return res if format is False else moeda(res)


def dobro(preco, format=False):
    res = preco * 2
    return res if format is False else moeda(res)


def metade(preco, format=False):
    res = preco / 2
    return res if format is False else moeda(res)


def resumo(preco, taxaAumento=0, taxaReducao=0):
    print('~' * 30)
    print('Resumo do Valor'.center(30))
    print('~' * 30)
    print(f'Preço Analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaAumento}% de aumento: \t{aumentar(preco, taxaAumento, True)}')
    print(f'{taxaReducao}% de redução: \t{diminuir(preco, taxaReducao, True)}')
    print('~' * 30)


def moeda(preco = 0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')