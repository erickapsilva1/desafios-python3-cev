# programa que lê números e cria
# uma lista completa
# uma só com pares
# uma apenas com ímpares

listnums = list()
listpar = list()
listimpar = list()
resp = ''

while True:
    num = int(input('Digite um número: '))
    listnums.append(num)
    if num % 2 == 0:
        listpar.append(num)
    else:
        listimpar.append(num)
    resp = input('Quer continuar? [S/N]')
    if resp.upper() == 'N':
        break

print('=-='*20)
print(f'Sua lista é {listnums}')
print(f'Os números pares são: {listpar}')
print(f'Os números ímpares são: {listimpar}')