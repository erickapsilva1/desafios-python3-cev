# programa que tenha uma tupla com várias palavras (não usar acentos),
# depois disso, ele deve mostrar apenas as vogais

palavras = ('Amora', 'Paralelepipedo', 'Pneumoultramicroscopicossilicovulcanoconiose', 'Cabra', 'Tchau')
for nome in palavras:
    print(f'Na palavra {nome.upper()} temos: ',end='')
    for l in range(0, len(nome)):
        if nome[l] == 'a' or nome[l] == 'e' or nome[l] == 'i' or nome[l] == 'o' or nome[l] == 'u':
            print(nome[l].upper(),end=' ')
    print('\n')