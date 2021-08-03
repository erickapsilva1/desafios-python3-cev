# programa que lê 8 números e grava numa lista
# essa lista deve gerar outras duas listas: um com num pares e outro com ímpares

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
print(f'Todos os valores: {num}')
print(f'Pares: {num[0]}')
print(f'Ímpares: {num[1]}')