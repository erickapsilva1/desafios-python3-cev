'''
Sortear um de 4 alunos. Escreva e sorteie um deles.
'''
import random
aluno1 = input("Nome: ")
num1 = 1
aluno2 = input("Nome: ")
num2 = 2
aluno3 = input("Nome: ")
num3 = 3
aluno4 = input("Nome: ")
num4 = 4

msg = "Aluno escolhido: "
sorteio = random.randint(1,4)

if sorteio == num1:
    print(msg,aluno1)
elif sorteio == num2:
    print(msg,aluno2)
elif sorteio == num3:
    print(msg,aluno3)
elif sorteio == num4:
    print(msg,aluno4)



