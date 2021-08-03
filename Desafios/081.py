# programa que lê vários números e add numa lista
# mostra:
# - quantos elementos tem
# - ordenar por forma decrescente
# - se o valor 5 faz parte

listanum = list()
resp = ""

while True:
    num = int(input('Digite um número: '))
    listanum.append(num)
    resp = input('Quer continuar? [S/N)')
    if resp.upper() == "N":
        break

listanum.sort(reverse=True)

print(f'Números digitados {listanum}')

if 5 in listanum:
    print("Tem o número 5!")
else:
    print("Não tem o número 5!")