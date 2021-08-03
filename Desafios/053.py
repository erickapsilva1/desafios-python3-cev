# programa que leia uma frase qualquer e diga se ela é palíndromo,
# desconsiderando os espaços

# elimina espaços antes e depois, joga para maiúsculas:
frase = str(input('Digite uma frase: ')).strip().upper()

# separa as palavras
palavras = frase.split()

# junta elas
junto = ''.join(palavras)

inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('A sentença: ')
    print(junto, inverso)
    print('É palíndromo')
else:
    print('A sentença: ')
    print(junto, inverso)
    print('Não é palíndromo')

# imprime
# print('Você digitou a frase {}'.format(junto))
