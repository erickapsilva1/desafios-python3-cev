# programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência
# no final mostre a listagem de forma tabular

prodPreco = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.50,
             'Compasso', 9.99, 'Mochila', 120.32, 'Livro', 34.50)

for item in range(0, len(prodPreco),2):
    print(prodPreco[item], '......', prodPreco[item+1])

#print(prodPreco)