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


def test():
    pass


def moeda(preco = 0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')