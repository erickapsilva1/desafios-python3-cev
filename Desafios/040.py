# programa que calcule a média do aluno
# dadas 2 notas (abaixo de 5 é reprovado, entre 5 e 6.9 recuperação
# e acima de 7 é aprovado)

n1 = float(input('N1: '))
n2 = float(input('N2: '))
ma = (n1 + n2) / 2

if ma < 5.0:
    print('REPROVADO! Média: {}'.format(ma))
elif ma >= 5.0 and ma <= 6.9:
    print('RECUPERAÇÃO! {}'.format(ma))
elif ma >= 7.0:
    print('APROVADO! {}'.format(ma))
else:
    print('Algo deu errado...')