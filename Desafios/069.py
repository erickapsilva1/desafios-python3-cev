# programa que leia a idade e sexo de várias pessoas
# a cada pessoa cadastrada, o programa deverá perguntar se o usuários quer ou não continuar
# no final mostre:
# a) quantas pessoas tem mais de 18 anos
# b) quantos homens foram cadastrados
# c) quantas mulheres tem menos de 20 anos

totDez = 0
totH = 0
totM = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M]')).strip().upper()[0]

    if idade >= 18:
        totDez += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N:]')).strip().upper()[0]
    if resp == 'N':
        break
print('Acabou')
print('Total de pessoas com mais de 18 anos: ', totDez)
print('Total de homens: ', totH)
print('Total de mulheres com menos de 20 anos: ', totM)