# Crie um programa que leia o nome de uma
# pessoa e diga se ela tem "Silva"
# no nome.

nome = input('Esreve o nome: ')
if nome.find('Silva') > 0:
    print('O nome {} tem SILVA'.format(nome))
else:
    print('O nome {} não tem SILVA'.format(nome))
