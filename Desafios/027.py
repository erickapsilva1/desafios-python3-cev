# programa que leia o nome de uma
# pessoa, mostrando em seguida
# 1º e último nome separamente.

fullname = input('Full Name: ')
print('First Name: ', fullname.split(' ')[0])
print('Last Name: ', fullname.split(' ')[-1])
