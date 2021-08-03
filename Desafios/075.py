# programa que leia 4 valores e coloque numa tupla, e mostre:
# a) quantas vezes apareceu o valor 9
# b) em que posição apareceu o primeiro valor 3
# c) quais foram os números pares

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))
num4 = int(input('Digite um número: '))

numeros = (num1, num2, num3, num4)

cont = 0

for num in range(0, len(numeros)):
    if numeros[num] % 2 == 0:
        cont += 1
    # print(num, f': {numeros[num]}')

print('Números digitados: ', numeros)
print('O valor 9 apareceu: ', numeros.count(9))
print('O valor 3 apareceu na posição: ', numeros.index(3) + 1)
print('Valores pares: ', cont)

