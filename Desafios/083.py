# programa que lê uma expressão e enalisa se ela está correta ou não

userStr = input('Digite uma expressão: ')
openStr = userStr.count('(')
closeStr = userStr.count(')')

if openStr == closeStr:
    print('OK!')
else:
    print('NOK!')
    if openStr > closeStr:
        print(f'Precisa fechar {openStr - closeStr} parentesis')
    else:
        print(f'Precisa abrir {closeStr - openStr} parentesis')
