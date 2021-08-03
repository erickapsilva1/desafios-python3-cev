# refazer o ex. 051
# porém, usando while

pt = int(input('Informe o 1º termo: '))
rz = int(input('Informe a razão: '))
termo = pt
cont = 1

while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += rz
    cont += 1

print('FIM')