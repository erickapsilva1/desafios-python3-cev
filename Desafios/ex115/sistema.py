from Desafios.ex115.lib.interface import *
from Desafios.ex115.lib.arquivo import *
from time import sleep

arq = 'cev.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

cabecalho('SISTEMA ARQUIVO V1.0')
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair'])
    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo... Até logo.')
        break
    else:
        print(f'\033[31mOpção inválida!\033[m')
    sleep(1)




