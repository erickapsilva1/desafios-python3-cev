# ler o ano de nascimento de um atela e mostre a sua categoria
# 9 mirim, 14 infatil, 19 junior, 20 sênior, acima master

import time

idade = int(input('Informe o ano de nascimento: '))
ano = int(time.strftime('%Y'))
idade = ano - idade

if idade <= 9:
    print('{} anos: MIRIM'.format(idade))
elif idade > 9 and idade < 15:
    print('{} anos: INFANTIL'.format(idade))
elif idade > 15 and idade < 20:
    print('{} anos: JUNIOR'.format(idade))
elif idade == 20:
    print('{} anos: SÊNIOR'.format(idade))
elif idade > 20:
    print('{} anos: MASTER'.format(idade))