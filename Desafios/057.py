# programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
# caso esteja errado, peça a digitação novamente até ter um valor correto


sexo = str(input('Digite o sexo [F] ou [M]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Errado! Informe novamente: ')).strip().upper()[0]
print('OK')