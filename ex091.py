from random import randint
from operator import itemgetter
from time import sleep
dado = {'Jogador 1':randint(1,6),
        'Jogador 2':randint(1,6),
        'Jogador 3':randint(1,6),
        'Jogador 4':randint(1,6)}
print('=-'*15)
for keys, value in dado.items():
    sleep(1.5)
    print(f'{keys} tirou o numero: {value}')
print('=-'*15)
print('======== Ranking dos Jogadores ========')
n = 1
for keys, values in sorted(dado.items(), key=itemgetter(1), reverse=True):
    sleep(1.5)
    print(f'{n}º - {keys}: {values}')
    n+=1
# Antes eu usei o "dado.items(), key=lambda item:item[1], reverse=True"; funcionou da mesma forma e me atendeu perfeiramente
