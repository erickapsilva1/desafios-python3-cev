# refazer o ex. 009, só que com laço for

tab = int(input('Tabuada: '))

for c in range(0, 11):
    print(tab,' x ', c , ' = {}'.format(tab * c))