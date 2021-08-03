# programa que leia ano de nascimento de sete pessoas.
# no final, mostre quantas pessoas ainda não atingiram a maioridade
# quantas já são maiores
from datetime import date

atual = date.today().year
tMaior = 0
tMenor = 0

for pessoa in range(1, 8):
    nasc = int(input('Ano de nascimento da {}ª pessoa: '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        tMaior += 1
    else:
        tMenor += 1

print('De maior: ', tMaior)
print('De menor: ', tMenor)