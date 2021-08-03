# preecher uma lista de números de acordo
# com a vontade do usuário

listanum = list()
resp = 0

while True:
    num = (int(input(f'Digite um valor: ')))
    if num in listanum:
        print(f'Este número já está na lista.')
    else:
        listanum.append(num)
        print(f'Valor adicionado com sucesso...')
    resp = input(f'Quer continuar? [S/N]')
    if resp.upper() == "N":
        break

listanum.sort()
print(f'Numeros digitado {listanum}')