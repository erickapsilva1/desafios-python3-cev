# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possiveis sobre ele.

n = input('Digite algo: ')

print('Vamos analisar muitas coisas sobre o que você escreveu para nós...')
print('O tipo de',n,'é:',type(n))
print('Está em minúsculo?', n.islower())
print('Está em maiúsculo?', n.isupper())
print('É um número?',n.isnumeric())
print('É um texto?',n.isalpha())
print('É alfanumético?',n.isalnum())
print('Vamos deixar as primeiras letras em maiúsculo?', n.capitalize())
print('É decimal?',n.isdecimal())
print('É um dígito?',n.isdigit())
print("É espaço?",n.isspace())
