# programa que calcula preço de viagem, sendo 0,50 por km em rolês até 200km
# e 0,45 para acima dessa km.

role = int(input('Qual a distância da viagem: '))
if role <= 200:
    print('Total: R$', role * 0.50)
else:
    print('Total: R$', role * 0.45)