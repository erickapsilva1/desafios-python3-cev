import moeda

p = float(input('Digite o preço: R$'))
print(f'Metade: {moeda.metade(p)}')
print(f'Dobro: {moeda.dobro(p)}')
print(f'Aumento de 12%: {moeda.aumentar(p, 12)}')
print(f'Redução de 18%: {moeda.diminuir(p, 18)}')