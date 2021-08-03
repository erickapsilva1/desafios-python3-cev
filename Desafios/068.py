# programa que jogue par ou impar e só pare caso o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou.

from random import randint
v = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar: ')).strip().upper()[0]
    print('Você jogou {} e o PC jogou {}. Total de {}'.format(jogador, computador, total))
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('GAME OVER!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('GAME OVER!')
            break
    print('Vamos jogar novamente')
print('Você venceu {} vezes'.format(v))