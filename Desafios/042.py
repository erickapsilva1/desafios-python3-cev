# calcular se um triângulo é:
# equilátero (todos os lados iguais), ilósceles (dois lado iguais) ou escaleno (todos os lados diferentes)

r1 = float(input('1º segmento: '))
r2 = float(input('2º segmento: '))
r3 = float(input('3º segmento: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r3 == r2:
        print('ISÓSCELES')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('ESCALENO')
    else:
        print('Triângulo diferenciado...')
else:
    print('Isso não é um triângulo!')