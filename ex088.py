from random import randint
from time import sleep
print('='*40)
jogada = int(input('Digite quantas jogadas você deseja: '))
p = 1
print('='*40)
for i in range(jogada):
    lista_mega_sena = []
    for r in range(1,7):
        numeros = randint(1, 60)
        if numeros not in lista_mega_sena:
            lista_mega_sena.append(numeros)
        else:
            pass
        sleep(0.2)
    lista_mega_sena.sort()
    print(f'Jogo {p}: {lista_mega_sena}')
    p += 1
sleep(0.25)

