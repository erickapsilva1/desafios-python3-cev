# Programa que leia nome, sexo, idade de várias pessoas
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# no final mostre:
# a) qtas pessoas cadastradas
# b) a média de idade
# c) uma lista do mulheril
# d) uma lista com idade acima da média

pessoa = dict()
pessoas = list()
strResp = ''
strSexo = ''
idade = 0
media = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        strResp = str(input('Sexo [F/M/O]: ')).upper()[0]
        if strResp.upper() == 'F' or strResp.upper() == 'M' or strResp.upper() == 'O':
            pessoa['sexo'] = strResp.upper()
            break
        else:
            print('ERRO! Por favor, digite apenas M [Masculuno], F [Feminino] ou O [Outros]')
    while True:
        idade = str(input('Idade: '))
        if idade.isdigit():
            pessoa['idade'] = idade
            media += int(idade)
            break
        else:
            print('ERRO! Digite apenas números.')
    pessoas.append(pessoa.copy())
    pessoa.clear()
    strResp = str(input('Quer continuar? [S/N] '))
    if strResp.upper() != 'S':
        break
print('-=' * 50)
print(f'A) Ao todo temos {len(pessoas)} pessoa(s) cadastrada(s).')
print(f'B) A média de idade é de {media / len(pessoas):5.2f} ano(s).')
print(f'C) As mulheres cadastradas foram: ')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if int(p['idade']) > media / len(pessoas):
        print(f'nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')
print('<< ENCERRADO >>')