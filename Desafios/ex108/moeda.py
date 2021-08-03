def aumentar(preco, taxa):
    return moeda(preco + (preco * taxa) / 100)


def diminuir(preco, taxa):
    return moeda(preco - (preco * taxa) / 100)


def dobro(preco):
    return moeda(preco * 2)


def metade(preco):
    return moeda(preco / 2)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')