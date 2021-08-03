# solicitar inteiros e preencher uma matriz 3 x 3
# mostrando a soma dos valores pares
# a soma dos valores da 3ª coluna
# o maior valor da segunda coluna

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
somaterColuna = 0
maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite: '))
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
        if coluna == 2:
            somaterColuna += matriz[linha][coluna]
        if coluna == 1:
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^6}]',end='')
    print()
print('-='*30)
print(f'Soma valores pares = {soma}')
print(f'Soma valores da terceira coluna = {somaterColuna}')
print(f'O maior valor da segunda linha é: {maior}')