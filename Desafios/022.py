# programa que leia o nome completo
# e mostre:
# Nome com letras maiúsculas
# Nome com letras minúsculas
# Quantas letras
# Quantas letras tem o 1º nome

fullname = input('Nome completo: ')
print(fullname.upper())
print(fullname.lower())
print(len(fullname) - fullname.count((' ')))
print(len(fullname.split(' ')[0]))