import moeda

p = float(input('Digite o preço: R$'))
print(f'Metade: {moeda.metade(p, True)}')
print(f'Dobro: {moeda.dobro(p, True)}')
print(f'Aumento de 12%: {moeda.aumentar(p, 12, True)}')
print(f'Redução de 18%: {moeda.diminuir(p, 18, True)}')