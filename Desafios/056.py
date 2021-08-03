# programa que leia nome, idade e sexo de 4 pessoas
# no final do programa mostre:
# média de idade
# nome do homem mais velho
# quantas mulheres tem menos de 20 anos

media = 0
nHomemVelho = str
iHomemVelho = 0
qMulheres = 0

for i in range(1, 5):
    print('''=============
{} Pessoa 
============='''.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))

    media += idade

    if sexo == 'F':
        qMulheres += 1
    elif sexo == 'M':
        if i == 1:
            iHomemVelho = idade
            nHomemVelho = nome
        else:
            if idade > iHomemVelho:
                iHomemVelho = idade
                nHomemVelho = nome

print('Média de idade: {} anos'.format(media / 4))
print('Quantidade de mulheres: {}'.format(qMulheres))
print('Nome do homem mais velho: {}'.format(nHomemVelho))

