# faça uma lista ordenada sem repetições
# não pode usar o sort

lista = []

for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posicao {pos}')
                break
            pos += 1

print('=' * 50)
print(f'Os valores digitado em ordem foram {lista}')
