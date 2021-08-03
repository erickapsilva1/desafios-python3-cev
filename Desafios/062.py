# melhorar o desafio 61
# perguntando se o usuário quer mais termos, finalizando apenas se for = 0

pt = int(input('Informe o 1º termo: '))
rz = int(input('Informe a razão: '))
termo = pt
cont = 1
mais = 10
total = 0

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += rz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print('FIM. Com {} termos'.format(total))