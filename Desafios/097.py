# programa que tenha uma função escreva.
# que recebe um texto qualquer como parâmetro e moestre
# uma mensagem com tamanho adaptável

def escreva(texto):
    tam = len(texto) + 4
    print(tam * '-')
    print(f'  {texto}')
    print(tam * '-')


escreva("Olá Mundo!")
escreva(" Pneumoultramiscoscopocossicovulcanoconiose!!! ")
escreva("CeV")