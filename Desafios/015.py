# Programa que pergunta qtd. de KM percorridos. E a qtd de dias em que foi alugado.
# Calcular sabendo que o dia custa r$ 60 e o km 0,15

km = int(input('Informe KM: '))
dia = float(input('Dias locação: '))

v1 = km * 0.15
v2 = dia * 60.00

print('Serão cobrados R${:.2f} pelos {}KM e R${:.2f} pelos {} dias.'.format(v1,km,v2,dia))