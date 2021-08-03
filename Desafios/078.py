# programa que leia 5 números e informe:
# maior, menos e suas respectivas posicoes

mai = 0
men = 0

listanum = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posicao {c}:')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print('='*50)
print(f'Voce digitou os valores {listanum}')
print(f'Maior número: {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if listanum[i] == mai:
        print(f'{i}... ', end='')
print()
print(f'Menor numero: {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if listanum[i] == men:
        print(f'{i}...', end='')
