# programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionario
# com as seguintes infos:
# - qtd de notas
# - maior nota
# - menor nota
# - média da turma
# - a situação (opcional)
# add docstrings da function


def notas(*n, sit=False):
    """
    --> Faz o cálculo com notas fornecidas.
    :param n: notas, separadas por vírgula
    :param sit: se True, exibe a situação {EXCELENTE, BOA, RAZOÁVEL ou RUIM} de acordo com a média
    :return: uma lista
    """
    lista = dict()
    media = sum(n) / len(n)
    lista['total'] = len(n)
    lista['maior'] = max(n)
    lista['menor'] = min(n)
    lista['media'] = round(media, 2)
    if sit:
        if media < 5:
            lista['situacao'] = 'RUIM'
        elif media > 5 and media < 7:
            lista['situacao'] = 'RAZOÁVEL'
        elif media > 7 and media < 9:
            lista['situacao'] = 'BOA'
        else:
            lista['situacao'] = 'EXCELENTE'
    print(lista)


notas(6.9, 5.7, 7, 10, sit=True)
notas(10, 10, 10, sit=True)
notas(0, 0, 1, sit=True)
notas(10, 2, 7, 8.6)
help(notas)