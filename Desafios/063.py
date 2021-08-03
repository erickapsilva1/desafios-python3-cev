# faça a sequência de Fibonacci.
# recebendo n e fazendo n termos.

n1 = int(input('Digite o número: '))
val1 = 0
val2 = 1

print('{} -> {}'.format(val1, val2), end='')
cont = 3
while cont <= n1:
    val3 = val1 + val2
    print(' -> {}'.format(val3), end='')
    val1 = val2
    val2 = val3
    cont += 1
print(' -> FIM')