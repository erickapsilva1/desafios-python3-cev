'''
O professor quer sortear a ordem de apresentação de trabalhos.
Programa que leia o nome dos alunos e mostre a ordem.
'''
import random
alunos = [input('Aluno 1: '),input('Aluno 2: '),input('Aluno 3: '),input('Aluno 4: ')]

print('Ordem sorteada: ')

for i in range(len(alunos)):
    escolha = random.choice(alunos)
    print(escolha)
    alunos.remove(escolha)