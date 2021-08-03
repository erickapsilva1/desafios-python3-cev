# programa que mostre uma contagem regressiva de 10 até 0, com a pausa de 1 segundo

import time

print('Contagem regressiva...')
for c in range(10, 0, -1):
    print(c, '...')
    time.sleep(1)
print('CABUUUUUUUUM!!!')    