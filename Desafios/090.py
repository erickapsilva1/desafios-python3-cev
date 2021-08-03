# programa que leia o nome e a média de um aluno
# gravando a situação em um dicionário

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situacao'] = 'Reprovado'

print(aluno)

for k, v in aluno.items():
    print(f'{k} é igual a {v}')