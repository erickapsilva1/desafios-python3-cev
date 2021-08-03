# programa que tenha uma função chamada voto() que recebe como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório
# nas eleicoes

def voto(nascimento):
    from datetime import datetime
    idade = datetime.now().year - nascimento
    if idade < 16:
        return "NEGADO"
    elif 16 <= idade < 18 or idade > 65:
        return "OPCIONAL"
    else:
        return "OBRIGATÓRIO"


print(voto(1918))
print(voto(1991))
print(voto(2003))
print(voto(2009))

