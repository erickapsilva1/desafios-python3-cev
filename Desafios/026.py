# Programa que leia uma frase pelo
# teclado e mostre:

# Vezes que o A aparece
# Posicao que ela aparece a primeira vez
# Posicao que aparece a última vez.

frase = input('Digite uma frase: ')
frase = frase.upper()
print(frase.count('A'))
print(frase.find('A'))
print(frase.rfind('A'))
