# tupla que conta por extenso de 0 a 20
# o programa deve ler um número e mostrar por extenso.

numeros = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
           'Onze','Doze','Treze','Quatorza','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    num = int(input('Digite um número entre 0 a 20: '))
    if num > 0 and num < 21:
        print(numeros[num])
        break
    print('Tente novamente! Digite um número entre 0 a 20: ')