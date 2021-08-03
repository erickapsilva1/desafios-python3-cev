# programa que mostre a tabuada de vários números, um para cada valor digitado
# deverá ser interrompido caso o valor for negativo

tab = int(input('Tabuada de qual número: '))
cont = 0

while tab > 0:
    while cont < 11:
        print(tab,' x ', cont , ' = {}'.format(tab * cont))
        cont += 1
    cont = 0
    tab = int(input('Tabuada de qual número: '))
print('Até a próxima!')