# programa que leia ano bissexto

ano = int(input('Informe um ano: '))
if (ano / 4) == 503:
    print('Não')
else:
    print('Sim')