# tabela do campeonato brasileiro, depois mostre:
# a) apenas os 5 primeiros colocados
# b) os últimos 4 colocados
# c) lista em ordem alfabética
# d) em que posição está a Chapecoense

times = ('Flamengo', 'Fluminense', 'Atlérico Mineiro', 'Corinthians', 'Palmeiras', 'Sport Recife', 'América-MG',
         'São Paulo', 'Grêmio', 'Vasco da Gama', 'Internacional', 'Botafogo', 'Cruzeiro', 'EC Vitória', 'Santos',
         'Atlético-PR', 'Chapecoense', 'Bahia', 'Ceará SC', 'Paraná')
print('-=' * 30)
print('Classificação do Brasileirão: ', times)
print('-=' * 30)
print('5 primeiros colocados são: ', times[:4])
print('-=' * 30)
print('4 últimos colocado são: ', times[-4:])
print('-=' * 30)
print('Ordem alfabetica: ', sorted(times))
print('-=' * 30)
print('A Chape está na posição: ', times.index('Chapecoense') + 1)
print('-=' * 30)